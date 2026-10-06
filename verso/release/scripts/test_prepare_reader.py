#!/usr/bin/env python3
"""Small regression tests; the publication pass also checks all book paragraphs."""

import unittest
import json
from pathlib import Path
import tempfile
import shutil
import subprocess

from prepare_reader import annotation_node, insert_annotations, extract_alignment, parse, prepare_document, reading_prose, preserve_legacy_routes, card_citations, resolve_declaration_links, repair_search_link_resolution, repeated_section_header_ids, suppress_repeated_section_headers, join_reader_documents, join_reader_blocks, join_reader_pages, relocate_reader_footnote
from validate_reader import is_machine_mathlib_find_link


class ReaderTests(unittest.TestCase):
    def test_math_annotation_follows_display_not_its_introducing_sentence(self):
        document = parse('<section><p>The six models are:</p>'
                         '<code class="math inline">six models</code>'
                         '<code class="math display">six models</code><p>Next argument.</p>'
                         '<aside class="lean-annotation"><code class="math display">six models</code></aside>'
                         '<div class="namedocs"><code class="math display">six models</code></div></section>')
        before = reading_prose(parse('<html><main>' + document.html() + '</main></html>'))
        insert_annotations('C/Models', document, [dict(anchor_kind='math', after='six models',
            title='Checked classification', explanation=['Exactly six isomorphism classes.'])], {}, 'a' * 40, {})
        html = document.html()
        self.assertIn('<code class="math display">six models</code><aside', html)
        self.assertLess(html.index('Exactly six'), html.index('Next argument.'))
        self.assertEqual(before, reading_prose(parse('<html><main>' + html + '</main></html>')))

    def test_math_anchor_rejects_inline_only_and_ambiguous_displays(self):
        for html in ('<code class="math inline">models</code>',
                     '<code class="math display">models</code>' * 2):
            with self.assertRaisesRegex(ValueError, 'expected one prose anchor'):
                insert_annotations('C/Models', parse('<section>' + html + '</section>'),
                    [dict(anchor_kind='math', after='models', title='Classification', explanation=['Note.'])],
                    {}, 'a' * 40, {})

    def test_math_annotation_follows_native_display_paragraph_wrapper(self):
        document = parse('<section><p>The models are:</p>'
                         '<p>\n<code class="math display">models</code></p>'
                         '<p>Next argument.</p></section>')
        before = reading_prose(parse('<html><main>' + document.html() + '</main></html>'))
        insert_annotations('C/Models', document, [dict(anchor_kind='math', after='models',
            title='Classification', explanation=['Checked models.'])], {}, 'a' * 40, {})
        html = document.html()
        self.assertIn('</code></p><aside', html)
        self.assertEqual(before, reading_prose(parse('<html><main>' + html + '</main></html>')))

    def test_math_anchor_rejects_a_display_mixed_with_prose(self):
        document = parse('<section><p>Intro <code class="math display">models</code> clause.</p></section>')
        with self.assertRaisesRegex(ValueError, 'complete paragraph'):
            insert_annotations('C/Models', document, [dict(anchor_kind='math', after='models',
                title='Classification', explanation=['Checked models.'])], {}, 'a' * 40, {})

    def test_joined_blocks_have_one_unique_dependency_list_with_all_bookmarks(self):
        def dependencies(names, bookmark):
            return '<div class="lean-reference"><details class="implementation-references" id="' \
                + bookmark + '"><summary>Dependencies</summary><ul>' \
                + ''.join('<li><a href="https://example.org/' + name + '"><code>' + name
                          + '</code></a></li>' for name in names) + '</ul></details></div>'
        head = parse('<main><section><h1 id="C___Head">Head</h1><p>Original start.</p>'
                     + dependencies(['A', 'B'], 'old-head-dependencies') + '</section></main>')
        tail = parse('<main><section><h1 id="C___Tail">Tail</h1><p>Original end.</p>'
                     + dependencies(['B', 'C'], 'old-tail-dependencies') + '</section></main>')
        expected = reading_prose(head) + reading_prose(tail)
        join_reader_blocks(head, tail, dict(head='C/Head', tail='C/Tail',
                                           head_ends='start.', tail_starts='Original end.'))
        third = parse('<main><section><h1 id="C___Third">Third</h1><p>Final original sentence.</p>'
                      + dependencies(['C', 'D'], 'old-third-dependencies') + '</section></main>')
        expected += reading_prose(third)
        join_reader_blocks(head, third, dict(head='C/Head', tail='C/Third',
                                            head_ends='end.', tail_starts='Final original'))
        self.assertEqual(reading_prose(head), expected)
        disclosures = [n for n in head.walk() if n.has_class('implementation-references')]
        self.assertEqual(len(disclosures), 1)
        self.assertEqual(sorted(n.text() for n in disclosures[0].walk() if n.tag == 'code'),
                         ['A', 'B', 'C', 'D'])
        self.assertNotIn('open', disclosures[0].attrs)
        for bookmark in ('C___Tail', 'C___Third', 'old-head-dependencies',
                         'old-tail-dependencies', 'old-third-dependencies'):
            self.assertEqual(sum(n.attrs.get('id') == bookmark for n in head.walk()), 1)
        self.assertEqual(sorted(n.attrs['href'] for n in disclosures[0].walk() if n.tag == 'a'),
                         ['https://example.org/A', 'https://example.org/B',
                          'https://example.org/C', 'https://example.org/D'])

    def test_block_footnote_follows_content_between_top_and_bottom_navigation(self):
        head = parse('<html><main><div class="content-wrapper">'
                     '<nav class="prev-next-buttons">Top navigation</nav><section>'
                     '<h1 id="C___Head">Head</h1><p>Intro.</p></section>'
                     '<nav class="prev-next-buttons">Bottom navigation</nav></div></main></html>')
        tail = parse('<html><main><section><h1 id="C___Tail">Tail</h1>'
                     '<p>Final exercise part.</p></section><section class="reader-footnotes">'
                     '<p id="footnote-1">Complete note.</p></section></main></html>')
        join_reader_blocks(head, tail, dict(head="C/Head", tail="C/Tail",
                                          head_ends="Intro.", tail_starts="Final"))
        html = head.html()
        self.assertLess(html.index("Top navigation"), html.index("Final exercise part."))
        self.assertLess(html.index("Final exercise part."), html.index("Complete note."))
        self.assertLess(html.index("Complete note."), html.index("Bottom navigation"))

    def test_block_continuation_preserves_paragraphs_math_bookmarks_and_footnote(self):
        head = parse('<html><main><div class="content-wrapper"><section>'
                     '<h1 id="C___Head">Classification</h1><p>We will prove</p>'
                     '<div class="lean-reference">Dependencies.</div></section>'
                     '<div class="prev-next-buttons"><a rel="next" href="Tail/">Tail</a></div>'
                     '</div></main></html>')
        tail = parse('<html><main><span id="Old-tail"></span><div class="content-wrapper"><section>'
                     '<h1 id="C___Tail">Theorem</h1><p>Theorem. Original statement.</p>'
                     '<code class="math display">A = 2I - R</code>'
                     '<p>Original conclusion.<sup class="footnote-reference">1</sup></p></section>'
                     '<section class="reader-footnotes"><h2>Notes</h2><ol>'
                     '<li id="footnote-1"><div class="footnote-body"><p>Complete original footnote.</p>'
                     '</div><a href="Tail/#footnote-ref-1">Return</a></li></ol></section>'
                     '<div class="prev-next-buttons"><a rel="next" href="Next/">Next</a></div>'
                     '</div></main></html>')
        expected = reading_prose(head) + reading_prose(tail)
        join_reader_blocks(head, tail, dict(head="C/Head", tail="C/Tail",
                                          head_ends="We will prove", tail_starts="Theorem."))
        self.assertEqual(reading_prose(head), expected)
        self.assertIn('<p>We will prove</p>', head.html())
        self.assertIn('<p>Theorem. Original statement.</p>', head.html())
        self.assertEqual(sum(n.tag == "h1" for n in head.walk()), 1)
        self.assertIn('id="C___Tail"', head.html())
        self.assertIn('id="Old-tail"', head.html())
        self.assertIn("Complete original footnote.", head.html())
        self.assertIn('href="Next/"', head.html())
        wrapper = next(n for n in head.walk() if n.has_class("content-wrapper"))
        self.assertTrue(wrapper.children[-2].has_class("reader-footnotes"))

    def test_diagram_list_continuation_restores_one_uninterrupted_list(self):
        head = parse('<html><main><section><h1 id="C___Head">Diagrams</h1>'
                     '<ul><li><p>A:</p><code class="math display">A diagram</code></li>'
                     '<li><p>D:</p><code class="math display">D diagram</code></li></ul>'
                     '<aside class="lean-annotation"><p>Classification explanation.</p></aside>'
                     '</section></main></html>')
        tail = parse('<html><main><section><h1 id="C___Tail">Continuation</h1>'
                     '<ul><li><p>E:</p><code class="math display">E diagram</code></li></ul>'
                     '<p>(a) Compute the determinant.</p></section></main></html>')
        expected = reading_prose(head) + reading_prose(tail)
        join_reader_blocks(head, tail, dict(head="C/Head", tail="C/Tail",
            head_ends="D diagram", tail_starts="E:", merge_lists=True,
            head_list=["A:", "D:"], tail_list=["E:"]))
        self.assertEqual(reading_prose(head), expected)
        lists = [n for n in head.walk() if n.tag == "ul"]
        self.assertEqual(len(lists), 1)
        self.assertEqual(sum(n.tag == "li" for n in lists[0].walk()), 3)
        self.assertIn('id="C___Tail"', lists[0].html())
        self.assertNotIn("lean-annotation", lists[0].html())
        self.assertLess(head.html().index("E diagram"), head.html().index("Classification explanation."))

    def test_nested_native_footnote_moves_after_all_continued_blocks(self):
        head = parse('<html><main><div class="content-wrapper"><section>'
                     '<h1 id="C___Head">Classification</h1><p>Intro.</p>'
                     '</section><div class="prev-next-buttons">Next</div></div></main></html>')
        tail = parse('<html><main><section><h1 id="C___Tail">Continuation</h1>'
                     '<p>(e) Graphs below.</p><section class="reader-footnotes">'
                     '<ol><li id="footnote-1"><div class="footnote-body"><p>Full note.</p>'
                     '</div></li></ol></section></section></main></html>')
        join_reader_blocks(head, tail, dict(head="C/Head", tail="C/Tail",
                                          head_ends="Intro.", tail_starts="(e)"))
        third = parse('<html><main><section><h1 id="C___Graphs">Graphs</h1>'
                      '<code class="math display">Affine diagrams.</code></section></main></html>')
        join_reader_blocks(head, third, dict(head="C/Head", tail="C/Graphs",
                                           head_ends="Graphs below.", tail_starts="Affine"))
        self.assertEqual(reading_prose(head), ["Intro.", "(e) Graphs below.", "Affine diagrams."])
        self.assertEqual(sum(n.has_class("reader-footnotes") for n in head.walk()), 1)
        section = next(n for n in head.walk() if n.tag == "section")
        self.assertFalse(any(n.has_class("reader-footnotes") for n in section.walk()))
        self.assertLess(head.html().index("Affine diagrams."), head.html().index("Full note."))

    def test_head_footnote_follows_the_entire_joined_reading_content(self):
        for nested in (False, True):
            with self.subTest(nested=nested):
                note = ('<section class="reader-footnotes"><ol><li id="footnote-head">'
                        '<p>Complete head note.</p><a href="#footnote-ref-head">Return</a>'
                        '</li></ol></section>')
                section = ('<section><h1 id="C___Head">Head</h1><p>Definition.</p>'
                           + (note if nested else '') + '</section>')
                head = parse('<html><main><div class="content-wrapper">' + section
                             + ('' if nested else note)
                             + '<nav>Navigation</nav></div></main></html>')
                tail = parse('<html><main><section><h1 id="C___Tail">Tail</h1>'
                             '<p>Continued discussion.</p></section></main></html>')
                join_reader_blocks(head, tail, dict(head="C/Head", tail="C/Tail",
                    head_ends="Definition.", tail_starts="Continued discussion."))
                self.assertEqual(reading_prose(head), ['Definition.', 'Continued discussion.'])
                self.assertLess(head.html().index('Continued discussion.'),
                                head.html().index('Complete head note.'))
                self.assertEqual(sum(n.attrs.get('id') == 'footnote-head' for n in head.walk()), 1)
                self.assertIn('href="#footnote-ref-head"', head.html())
                wrapper = next(n for n in head.walk() if n.has_class('content-wrapper'))
                self.assertTrue(wrapper.children[-2].has_class('reader-footnotes'))

    def test_block_continuation_rejects_boundary_or_list_drift(self):
        for changed in (dict(head_ends="Wrong boundary"), dict(head_list=["Wrong label:"])):
            head = parse('<html><main><section><h1 id="C___Head">Head</h1>'
                         '<ul><li><p>A:</p></li></ul></section></main></html>')
            tail = parse('<html><main><section><h1 id="C___Tail">Tail</h1>'
                         '<ul><li><p>E:</p></li></ul></section></main></html>')
            record = dict(head="C/Head", tail="C/Tail", head_ends="A:", tail_starts="E:",
                          merge_lists=True, head_list=["A:"], tail_list=["E:"])
            record.update(changed)
            with self.assertRaises(ValueError):
                join_reader_blocks(head, tail, record)

    def test_block_continuation_rejects_duplicate_footnote_bookmarks(self):
        head = parse('<html><main><section><h1 id="C___Head">Head</h1><p>Intro.</p>'
                     '</section><section class="reader-footnotes"><p id="footnote-1">First note.</p>'
                     '</section></main></html>')
        tail = parse('<html><main><section><h1 id="C___Tail">Tail</h1><p>Theorem.</p>'
                     '</section><section class="reader-footnotes"><p id="footnote-1">Second note.</p>'
                     '</section></main></html>')
        with self.assertRaisesRegex(ValueError, "duplicate footnote"):
            join_reader_blocks(head, tail, dict(head="C/Head", tail="C/Tail",
                                              head_ends="Intro.", tail_starts="Theorem."))

    def test_multiple_block_continuations_share_one_head_and_reject_tail_reuse(self):
        with tempfile.TemporaryDirectory(prefix="etingof-block-joins-") as folder:
            root = Path(folder)
            sections = {}
            for label, body in (("Head", "Intro."), ("First", "Theorem."), ("Second", "Exercises.")):
                (root / label).mkdir()
                (root / label / "index.html").write_text('<html><main><section>'
                    f'<h1 id="C___{label}">{label}</h1><p>{body}</p></section></main></html>')
                sections[f"C___{label}"] = [dict(address=f"/{label}/")]
            (root / "xref.json").write_text(json.dumps({
                "Verso.Genre.Manual.section": {"contents": sections}}))
            records = [dict(kind="blocks", head="C/Head", tail="C/First",
                            head_ends="Intro.", tail_starts="Theorem."),
                       dict(kind="blocks", head="C/Head", tail="C/Second",
                            head_ends="Theorem.", tail_starts="Exercises.")]
            joins = root / "joins.json"
            joins.write_text(json.dumps(records))
            self.assertEqual(join_reader_pages(root, joins, {}),
                             {"First/": "Head/", "Second/": "Head/"})
            document = parse((root / "Head/index.html").read_text())
            self.assertEqual(reading_prose(document), ["Intro.", "Theorem.", "Exercises."])
            joins.write_text(json.dumps([dict(kind="invalid", head="C/Head", tail="C/First")]))
            with self.assertRaisesRegex(ValueError, "unknown reader continuation kind"):
                join_reader_pages(root, joins, {})
            joins.write_text(json.dumps([records[1], records[1]]))
            # Avoid an already-joined-boundary failure masking the overlapping
            # record check: the first join's boundary is now the current end.
            records[1]["head_ends"] = "Exercises."
            joins.write_text(json.dumps([records[1], records[1]]))
            with self.assertRaisesRegex(ValueError, "overlapping reader continuation"):
                join_reader_pages(root, joins, {})

    def test_standalone_footer_becomes_linked_note_without_losing_its_proof(self):
        head = parse('<html><main><div class="content-wrapper"><section><h1 id="C___Head">Proof</h1>'
                     '<p>Equality holds.<code class="math inline">{}^2</code> Next sentence.</p>'
                     '</section><nav class="prev-next-buttons">Next</nav></div></main></html>')
        tail = parse('<html><main><span id="Old-footer"></span><section>'
                     '<h1 id="C___Footer">Footer</h1>'
                     '<p><code class="math inline">{}^2</code>Another argument.</p>'
                     '<aside class="lean-annotation"><p>Checked explanation.</p></aside>'
                     '<div class="lean-reference">Proof dependencies.</div>'
                     '</section></main></html>')
        record = dict(head="C/Head", tail="C/Footer", marker="{}^2", number="2",
                      tail_starts="{}^2Another argument.")
        relocate_reader_footnote(head, tail, record, "Proof/")
        self.assertEqual(reading_prose(head), ["Equality holds. Next sentence."])
        self.assertIn('id="C___Footer"', head.html())
        self.assertIn('id="Old-footer"', head.html())
        self.assertIn('href="Proof/#footnote-C___Footer"', head.html())
        self.assertIn('value="2"', head.html())
        self.assertIn('aria-label="Return to text"', head.html())
        self.assertIn("Another argument.", head.html())
        self.assertIn("Checked explanation.", head.html())
        self.assertNotIn("{}^2", head.html())
        self.assertEqual(sum(n.has_class("footnote-body") for n in head.walk()), 1)
        wrapper = next(n for n in head.walk() if n.has_class("content-wrapper"))
        self.assertTrue(wrapper.children[-2].has_class("reader-footnotes"))
        self.assertTrue(wrapper.children[-1].has_class("prev-next-buttons"))

    def test_footer_relocation_rejects_drift_or_ambiguous_reference(self):
        for marker in ("", '<code class="math inline">{}^2</code>' * 2):
            head = parse('<html><main><p>Proof.' + marker + '</p></main></html>')
            tail = parse('<html><main><p>Original footnote.</p></main></html>')
            with self.assertRaisesRegex(ValueError, "unique reference"):
                relocate_reader_footnote(head, tail, dict(tail="C/Footer", marker="{}^2",
                    number="2", tail_starts="Original footnote."))

    def test_prose_only_review_suppresses_fallback_but_preserves_alignment(self):
        html = ('<html><head></head><main><section><h2 id="Chapter5___Introduction">Introduction</h2>'
                '<p>Original book prose.</p><section>'
                '<h3 id="Chapter5___Introduction___formalization">Formalization</h3>'
                '<div class="namedocs"><pre class="signature">'
                '<span data-binding="const-Example.identification">Example.identification</span></pre>'
                '<div class="text"><p>Every simple module is identified with a membership-defined subtype.</p>'
                '<ul><li>book-ref=Chapter5/Introduction; role=primary</li></ul></div></div>'
                '</section></section></main></html>')
        pending = parse(html)
        prepare_document(pending, {}, "a" * 40, {})
        self.assertTrue(any(node.has_class("lean-statement") for node in pending.walk()))
        document = parse(html)
        before = reading_prose(document)
        ledger, _, inserted = prepare_document(document, {}, "a" * 40, {},
                                               book_prose_only=frozenset({"Chapter5/Introduction"}))
        self.assertEqual(reading_prose(document), before)
        self.assertEqual(inserted, 0)
        self.assertFalse(any(node.has_class("lean-statement") or node.has_class("implementation-references")
                             for node in document.walk()))
        self.assertNotIn("membership-defined", document.html())
        self.assertEqual(ledger, [dict(declaration="Example.identification",
                                      reference="Chapter5/Introduction", role="primary", imported=False)])

    def test_reviewed_page_break_rejoins_sentence_and_preserves_bookmarks_and_navigation(self):
        head = parse('<html><main><section><h1 id="C___Head">Problem</h1>'
                     '<p><em>Problem.</em> Leads to a</p><div class="lean-reference">Dependencies.</div></section>'
                     '<nav><a rel="next" href="Tail/">Continuation</a></nav></main></html>')
        tail = parse('<html><main><span id="Old-tail"></span><section>'
                     '<h1 id="C___Tail">Continuation</h1><p>new proof.</p>'
                     '<p>Next part.</p><aside class="lean-annotation"><p>Checked explanation.</p></aside>'
                     '</section><nav><a rel="next" href="Next/">Next</a></nav></main></html>')
        record = dict(head="C/Head", tail="C/Tail", head_ends="Leads to a", tail_starts="new proof.")
        join_reader_documents(head, tail, record)
        self.assertEqual(reading_prose(head), ["Problem. Leads to a new proof.", "Next part."])
        self.assertEqual(sum(node.tag == "h1" for node in head.walk()), 1)
        self.assertIn('id="C___Tail"', head.html())
        self.assertIn('id="Old-tail"', head.html())
        self.assertIn('<em>Problem.</em>', head.html())
        self.assertIn('href="Next/"', head.html())
        self.assertIn("Checked explanation.", head.html())
        section = next(n for n in head.walk() if n.tag == "section")
        self.assertTrue(section.children[-1].has_class("lean-reference"))

    def test_unreviewed_sentence_boundary_is_rejected(self):
        head = parse('<html><main><p>Wrong seam.</p></main></html>')
        tail = parse('<html><main><p>new proof.</p></main></html>')
        with self.assertRaisesRegex(ValueError, "reviewed sentence boundary"):
            join_reader_documents(head, tail, dict(head="C/Head", tail="C/Tail",
                                                   head_ends="Leads to a", tail_starts="new proof."))

    def test_validation_rejects_machine_mathlib_find_destinations(self):
        url = "https://leanprover-community.github.io/mathlib4_docs/find/?pattern=minpoly"
        self.assertTrue(is_machine_mathlib_find_link(url))
        self.assertFalse(is_machine_mathlib_find_link(url + "#doc"))
        self.assertFalse(is_machine_mathlib_find_link(url + "#src"))
        self.assertFalse(is_machine_mathlib_find_link("https://github.com/owner/repo/blob/rev/Proof.lean"))

    def test_list_notes_follow_the_complete_list_without_interrupting_items(self):
        for tag in ("ul", "ol"):
            with self.subTest(tag=tag):
                document = parse('<html><head></head><main><section><h1 id="Chapter5___Types">Types</h1>'
                                 '<p>We say that V is</p>' + f'<{tag}>'
                                 '<li><p>of complex type if not self-dual,</p></li>'
                                 '<li><p>of real type if symmetric,</p></li>'
                                 '<li><p>of quaternionic type if skew.</p></li>'
                                 f'</{tag}><p>Next passage.</p></section></main></html>')
                before = reading_prose(document)
                notes = [{"after": "of complex type", "anchor_kind": "list", "title": title,
                          "explanation": ["The forms are complex bilinear."]}
                         for title in ("The three types", "The form conventions")]
                _, _, inserted = prepare_document(document, {"Chapter5/Types": notes}, "a" * 40, {})
                self.assertEqual(inserted, 2)
                self.assertEqual(reading_prose(document), before)
                section = next(node for node in document.walk() if node.tag == "section")
                sequence = [node for node in section.children if hasattr(node, "tag")]
                self.assertEqual([node.tag for node in sequence], ["h1", "p", tag, "aside", "aside", "p"])
                self.assertEqual(sequence[2].html().count('<li>'), 3)
                self.assertNotIn('lean-annotation', sequence[2].html())
                self.assertIn("The three types", sequence[3].text())
                self.assertIn("The form conventions", sequence[4].text())

    def test_table_notes_follow_their_own_tables(self):
        document = parse('<html><head></head><main><section><h1 id="Chapter4___Tables">Tables</h1>'
                         '<p>Original introduction.</p><table><tr><th>S_3</th><td>1</td></tr></table>'
                         '<table><tr><th>A_5</th><td>3</td></tr></table></section></main></html>')
        before = reading_prose(document)
        notes = [{"after": group, "anchor_kind": "table", "title": group + " explained",
                  "explanation": ["Checked character calculation."]} for group in ("S_3", "A_5")]
        _, _, inserted = prepare_document(document, {"Chapter4/Tables": notes}, "a" * 40, {})
        self.assertEqual(inserted, 2)
        self.assertEqual(reading_prose(document), before)
        section = next(node for node in document.walk() if node.tag == "section")
        sequence = [(node.tag, node.text()) for node in section.children if hasattr(node, "tag")]
        self.assertEqual([tag for tag, _ in sequence], ["h1", "p", "table", "aside", "table", "aside"])
        self.assertEqual(sequence[3][1].count("S_3 explained"), 1)
        self.assertEqual(sequence[5][1].count("A_5 explained"), 1)

    def test_unknown_annotation_anchor_kind_is_rejected(self):
        document = parse('<html><head></head><main><section><h1 id="Chapter4___Tables">Tables</h1>'
                         '<p>Original introduction.</p></section></main></html>')
        note = {"after": "Original", "anchor_kind": "tabble", "title": "Note", "explanation": []}
        with self.assertRaisesRegex(ValueError, "unknown reader anchor kind"):
            prepare_document(document, {"Chapter4/Tables": [note]}, "a" * 40, {})

    def test_validation_rejects_silently_omitted_editorial_notes(self):
        from contextlib import redirect_stdout
        from io import StringIO
        from validate_reader import validate
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "alignment.json").write_text("[]")
            (root / "xref.json").write_text("{}")
            (root / "index.html").write_text('<html><main></main></html>')
            report = dict(alignment_entries=0, reviewed_annotations=0,
                          footnotes=0, redirects=0, editorial_review=dict(annotations=1))
            (root / "reader-report.json").write_text(json.dumps(report))
            output = StringIO()
            with redirect_stdout(output), self.assertRaises(ValueError):
                validate(root)
            self.assertIn("HTML omits or duplicates authored reader annotations", output.getvalue())
            report["editorial_review"]["annotations"] = 0
            (root / "reader-report.json").write_text(json.dumps(report))
            self.assertEqual(validate(root)["errors"], 0)

    def test_structure_only_introduction_uses_its_registered_page(self):
        html = '<html><head></head><main><h1>Chapter</h1><p>Recall the action.</p></main></html>'
        note = {"after": "Recall the action.", "title": "The action extends linearly",
                "explanation": ["Extend the group action to the group algebra."]}
        annotations = {"Chapter4/Introduction": [note]}
        document = parse(html)
        before = reading_prose(document)
        _, _, inserted = prepare_document(document, annotations, "a" * 40, {},
                                           ("Chapter4/Introduction",))
        self.assertEqual(inserted, 1)
        self.assertEqual(reading_prose(document), before)
        self.assertIn(note["title"], document.html())
        unrelated = parse(html)
        _, _, inserted = prepare_document(unrelated, annotations, "a" * 40, {})
        self.assertEqual(inserted, 0)
        self.assertNotIn(note["title"], unrelated.html())

    def test_running_header_requires_exact_ancestor_and_keeps_proof_and_bookmark(self):
        repeated = "Chapter3___Corollary3___5___5___heading-1"
        distinct = "Chapter3___Other___heading-1"
        title = "3.5. Finite dimensional algebras"
        sections = {identifier: [dict(id=identifier, data=dict(title=heading, context=[
            dict(title=title), dict(title="Corollary"), dict(title=heading)]))]
            for identifier, heading in ((repeated, title), (distinct, "3.5. A different argument"))}
        headers = repeated_section_header_ids({"Verso.Genre.Manual.section": dict(contents=sections)})
        self.assertEqual(headers, {repeated})
        document = parse(f'<html><main><h1>Corollary</h1><p>Statement.</p>'
                         f'<section><h2 id="{repeated}">{title}</h2><p>Proof continues.</p>'
                         f'<h2 id="{distinct}">3.5. A different argument</h2></section></main></html>')
        before = reading_prose(document)
        self.assertEqual(suppress_repeated_section_headers(document, headers), 1)
        self.assertEqual(reading_prose(document), before)
        self.assertIn(f'<span id="{repeated}" aria-hidden="true">', document.html())
        self.assertIn(f'<h2 id="{distinct}">', document.html())

    def test_pending_primary_statements_are_collapsed_and_vague_cards_suppressed(self):
        def card(name, description):
            return ('<div class="namedocs" id="'+name+'"><pre class="signature">'
                    '<span data-binding="const-'+name+'">'+name+'</span></pre><div class="text">'
                    '<p>'+description+'</p><ul><li>book-ref=Chapter2/Item; role=primary</li></ul></div></div>')
        document = parse('<html><head></head><main><section><h2 id="Chapter2___Item">Item</h2>'
            '<p>Original prose.</p><section><h3 id="Chapter2___Item___formalization">Formalization</h3>'+
            card("Useful", "Every invariant subspace has an invariant complement.")+
            card("Vague", "An auxiliary linear endomorphism depending on the module.")+
            '</section></section></main></html>')
        prepare_document(document, {}, "a" * 40, {})
        details = [node for node in document.walk() if node.has_class("lean-statement")]
        self.assertEqual(len(details), 1)
        self.assertNotIn("open", details[0].attrs)
        self.assertEqual(details[0].children[0].text(), "Every invariant subspace has an invariant complement.")
        self.assertNotIn("An auxiliary linear endomorphism", document.html())
        self.assertIn("Definitions and proof dependencies (2)", document.html())

    @unittest.skipUnless(shutil.which("node"), "Node is needed to check the native search resolver")
    def test_search_resolves_sources_without_changing_book_prefix(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "-verso-search").mkdir()
            path = root / "-verso-search/search-box.js"
            path.write_text('export const resolveAgainstBase = (dest) => {\n'
                'const base = document.querySelector("base");\n'
                'if (!base) return dest;\n'
                'const baseNoSlash = base.href.endsWith("/") ? base.href.slice(0, -1) : base.href;\n'
                'const destNoSlash = dest.startsWith("/") ? dest.slice(1) : dest;\n'
                'return baseNoSlash + "/" + destNoSlash;\n};')
            repair_search_link_resolution(root)
            script = ('const document = {querySelector:()=>({href:"https://example.org/book/"})};\n' +
                      path.read_text() + '\nconsole.log(JSON.stringify([resolveAgainstBase("/Chapter/#item"),'
                      'resolveAgainstBase("https://github.com/owner/repo/blob/rev/Source.lean")]));')
            output = subprocess.check_output(["node", "--input-type=module", "-e", script], text=True)
            self.assertEqual(json.loads(output), ["https://example.org/book/Chapter/#item",
                                                 "https://github.com/owner/repo/blob/rev/Source.lean"])

    def test_definition_links_use_retained_card_or_real_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for route in ("Original", "Reviewed", "find"):
                (root / route).mkdir()
            def link(name):
                return (f'<a href="Original/#{name}"><span data-binding="const-{name}">'
                        f'{name}</span></a>')
            (root / "Original/index.html").write_text('<html><head></head><main>' +
                link("Retained") + link("RepresentationTheory.Removed") + '</main></html>')
            (root / "Reviewed/index.html").write_text('<html><head></head><main>'
                '<details class="lean-statement"><summary>Checked statement</summary>'
                '<div class="namedocs" id="retained-card"><pre class="signature">'
                '<span data-binding="const-Retained">Retained</span></pre></div></details></main></html>')
            xref = {"Verso.Genre.Manual.doc": {"contents": {
                "Retained": [dict(address="/Original/", id="Retained", data=None)],
                "RepresentationTheory.Removed": [dict(address="/Original/", id="Removed", data=None)]}}}
            (root / "find/index.html").write_text('<html><head></head><main></main><script>'
                'window.xref = ' + json.dumps(xref) + ';\nconst untouched = true;</script></html>')
            report = resolve_declaration_links(root, xref, "a" * 40,
                {"RepresentationTheory.Removed": "RepresentationTheory.RealSource"})
            self.assertEqual(report["retained_declarations"], 1)
            self.assertEqual(report["source_destinations"], 1)
            page = (root / "Original/index.html").read_text()
            self.assertIn('href="Reviewed/#retained-card"', page)
            self.assertIn('/blob/' + "a" * 40 + '/RepresentationTheory/RealSource.lean', page)
            self.assertNotIn('id="Removed"', page)
            snapshot = (root / "find/index.html").read_text()
            self.assertIn(json.dumps(xref), snapshot)
            self.assertIn('const untouched = true;', snapshot)
            self.assertEqual(xref["Verso.Genre.Manual.doc"]["contents"]["Retained"][0]["address"], "/Reviewed/")
            self.assertEqual(xref["Verso.Genre.Manual.doc"]["contents"]["RepresentationTheory.Removed"][0]["id"], "")

    def test_unretained_imported_definition_uses_mathlib_docs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.html").write_text('<html><head></head><main>'
                '<a href="Formalization/#Module"><span data-binding="const-Module">Module</span></a>'
                '</main></html>')
            xref = {"Verso.Genre.Manual.doc": {"contents": {"Module": [dict(address="/", id="Module", data=None)]}}}
            resolve_declaration_links(root, xref, "a" * 40, {})
            self.assertIn('https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module#doc',
                          (root / "index.html").read_text())
            self.assertEqual(xref["Verso.Genre.Manual.doc"]["contents"]["Module"][0]["address"],
                             'https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module#doc')

    def test_upstream_annotation_link_selects_human_documentation_view(self):
        block = annotation_node({"title": "Minimal polynomial", "explanation": [],
                                 "links": [{"name": "minpoly.isIntegrallyClosed_eq_field_fractions'",
                                            "label": "Integer coefficients"}]}, {}, "a" * 40, {})
        self.assertIn("find/?pattern=minpoly.isIntegrallyClosed_eq_field_fractions%27#doc", block.html())

    def test_notes_at_one_paragraph_keep_editorial_order(self):
        document = parse('<html><head></head><main><section><h2 id="Chapter2___Background">Background</h2>'
                         '<p>Original background prose.</p></section></main></html>')
        annotations = [{"after": "Original background prose.", "title": title,
                        "explanation": ["Original background prose. Explained here."]}
                       for title in ("First explanation", "Second explanation", "Third explanation")]
        before = reading_prose(document)
        _, _, inserted = prepare_document(document, {"Chapter2/Background": annotations}, "a" * 40, {})
        titles = [next(child for child in node.children if getattr(child, "tag", None) == "h2").text()
                  for node in document.walk() if node.has_class("lean-annotation")]
        self.assertEqual(titles, [note["title"] for note in annotations])
        self.assertEqual(inserted, 3)
        self.assertEqual(reading_prose(document), before)

    def test_statement_and_proof_need_a_distinguishing_anchor(self):
        html = ('<html><head></head><main><section><h2 id="Chapter3___Density">Density</h2>'
                '<p>(ii) Let V = the finite sum of simple modules.</p>'
                '<p>(ii) Let B_i be the image of the algebra.</p></section></main></html>')
        note = {"after": "(ii) Let", "title": "Independent block operators",
                "explanation": ["The statement prescribes all blocks at once."]}
        with self.assertRaisesRegex(ValueError, "found 2"):
            prepare_document(parse(html), {"Chapter3/Density": [note]}, "a" * 40, {})
        note["after"] = "(ii) Let V ="
        document = parse(html)
        before = reading_prose(document)
        _, _, inserted = prepare_document(document, {"Chapter3/Density": [note]}, "a" * 40, {})
        self.assertEqual(inserted, 1)
        self.assertEqual(reading_prose(document), before)
        rendered = document.html()
        self.assertLess(rendered.index("Independent block operators"), rendered.index("(ii) Let B_i"))

    def test_coverage_note_without_alignment_panel(self):
        document = parse('<html><head></head><main><section><h2 id="Chapter2___Background">Background</h2>'
                         '<p>Original background prose.</p></section></main></html>')
        annotation = {"after": "Original background prose.", "kind": "coverage_gap",
                      "title": "This background is not formalized", "explanation": ["No proof is supplied."]}
        before = reading_prose(document)
        _, _, inserted = prepare_document(document, {"Chapter2/Background": [annotation]}, "a" * 40, {})
        self.assertEqual(inserted, 1)
        self.assertEqual(reading_prose(document), before)
        self.assertIn("FORMALIZATION STATUS", document.html())
        self.assertNotIn("IN LEAN", document.html())
        self.assertNotIn("lean-statement", document.html())

    def test_rewording_structure_description_preserves_fields(self):
        card = parse('<div class="namedocs"><pre class="signature">structure Diagram</pre>'
                     '<div class="text"><p>An auxiliary structure.</p>'
                     '<div class="docstring-section"><pre class="signature">obj : Q → Type</pre>'
                     '<p>The space at each vertex.</p></div></div></div>').children[0]
        result = annotation_node({"title": "Vertex spaces", "explanation": [], "declarations": [{
            "name": "Diagram", "label": "Checked fields", "documentation": "A quiver representation."}]},
            {"Diagram": card}, "a" * 40, {})
        self.assertIn("obj : Q → Type", result.html())
        self.assertIn("The space at each vertex.", result.html())
        self.assertIn("A quiver representation.", result.html())
        self.assertNotIn("An auxiliary structure.", result.html())

    def test_field_citation_does_not_change_structure_role(self):
        card = parse('<div class="namedocs"><div class="text"><p>Structure description.</p>'
                     '<ul><li>book-ref=Chapter9/Definition9.6.2; role=primary</li></ul>'
                     '<div class="docstring-section"><div class="docs"><ul>'
                     '<li>book-ref=Chapter9/Definition9.6.2; role=supporting</li>'
                     '</ul></div></div></div></div>').children[0]
        self.assertEqual(card_citations(card), [('Chapter9/Definition9.6.2', 'primary')])
    def test_integrity_inventory_includes_formulas_and_tables(self):
        document = parse('<html><head></head><body><main><section><h1>Book</h1>'
                         '<p>The character values are:</p><code class="math display">χ(g) = tr ρ(g)</code>'
                         '<table><tr><th>Class</th><th>Character</th></tr>'
                         '<tr><td>identity</td><td>2</td></tr></table>'
                         '<div class="split-toc"><table><tr><td>Navigation</td></tr></table></div>'
                         '</section></main></body></html>')
        before = reading_prose(document)
        self.assertEqual(before, ['The character values are:', 'χ(g) = tr ρ(g)', 'ClassCharacteridentity2'])
        prepare_document(document, {}, "a" * 40, {})
        self.assertEqual(reading_prose(document), before)
    def test_renamed_title_preserves_old_route_and_anchor(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "New-title").mkdir()
            (root / "New-title/index.html").write_text('<html><body><main><p>Original prose.</p></main></body></html>')
            (root / "xref.json").write_text(json.dumps({"Verso.Genre.Manual.section": {"contents": {
                "Chapter2___Item": [{"address": "/New-title/", "id": "Chapter2___Item"}]}}}))
            legacy = root / "legacy.json"
            legacy.write_text(json.dumps({"routes": {"Old-title/": {
                "key": "Chapter2___Item", "anchors": ["Old-wrapper-anchor"]}}}))
            self.assertEqual(preserve_legacy_routes(root, legacy), {"Old-title/": "New-title/"})
            redirect = (root / "Old-title/index.html").read_text()
            self.assertIn('../New-title/', redirect)
            self.assertIn('location.search + location.hash', redirect)
            self.assertIn('id="Old-wrapper-anchor"', (root / "New-title/index.html").read_text())

    def test_legacy_route_cannot_overwrite_current_book_page(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for title in ("Old", "New"):
                (root / title).mkdir()
                (root / title / "index.html").write_text('<html><body><main>Book</main></body></html>')
            (root / "xref.json").write_text(json.dumps({"Verso.Genre.Manual.section": {"contents": {
                "Item": [{"address": "/New/", "id": "Item"}]}}}))
            legacy = root / "legacy.json"
            legacy.write_text(json.dumps({"routes": {"Old/": {"key": "Item", "anchors": []}}}))
            with self.assertRaisesRegex(ValueError, "overwrite a current reading page"):
                preserve_legacy_routes(root, legacy)
    def test_multiparagraph_footnote(self):
        document = parse('<html><head></head><body><main><section><h1>Book</h1>'
                         '<p>Text<details class="footnote"><summary>[internal-id]</summary>'
                         '<p>First note paragraph.</p><p>Second note paragraph.</p>'
                         '</details> continues.</p></section></main></body></html>')
        before = reading_prose(document)
        _, count, _ = prepare_document(document, {}, "a" * 40, {})
        self.assertEqual(count, 1)
        self.assertEqual(reading_prose(document), before)
        body = next(node for node in document.walk() if node.has_class("footnote-body"))
        self.assertEqual(body.text(), "First note paragraph.Second note paragraph.")
        self.assertNotIn("internal-id", document.html())
        self.assertEqual(len([node for node in body.walk() if node.tag == "p"]), 2)

    def test_footnotes_stay_outside_checked_structure_fields(self):
        document = parse('<html><head></head><main><section><h1>Book</h1>'
                         '<p>Text<details class="footnote"><summary>[note]</summary>'
                         '<p>Complete book footnote.</p></details></p>'
                         '<aside class="lean-annotation"><h2>A unitary action</h2>'
                         '<details class="lean-statement"><summary>Checked structure</summary>'
                         '<div class="namedocs"><section class="docstring-section">'
                         '<p>Checked field description.</p></section></div></details></aside>'
                         '</section></main></html>')
        _, count, _ = prepare_document(document, {}, "a" * 40, {})
        self.assertEqual(count, 1)
        annotation = next(node for node in document.walk() if node.has_class("lean-annotation"))
        self.assertFalse(any(node.has_class("reader-footnotes") for node in annotation.walk()))
        footnotes = next(node for node in document.walk() if node.has_class("reader-footnotes"))
        self.assertIn("Complete book footnote.", footnotes.text())
        self.assertEqual([node.text() for node in annotation.walk() if node.tag == "h2"],
                         ["A unitary action"])

    def test_imported_alignment_is_preserved_not_printed(self):
        document = parse('<html><head></head><main><section><h1>Overview</h1>'
                         '<section><h2 id="Chapter2___Overview">Overview</h2><p>Original prose.</p>'
                         '<section><h3 id="Chapter2___Overview___formalization">Formalization</h3>'
                         '<p>Declaration: MonoidAlgebra</p>'
                         '<p>Alignment metadata: book-ref=Chapter2/Overview/Derived4; role=supporting</p>'
                         '</section></section></section></main></html>')
        rows = extract_alignment(document)
        self.assertEqual(rows, [dict(declaration="MonoidAlgebra", reference="Chapter2/Overview/Derived4",
                                     role="supporting", imported=True)])
        prepare_document(document, {}, "a" * 40, {})
        self.assertNotIn("book-ref=", document.html())
        self.assertIn("Definitions and proof dependencies (1)", document.html())
        self.assertEqual(reading_prose(document), ["Original prose."])

    def test_reviewed_anchor_must_match(self):
        document = parse('<html><head></head><main><section><h2 id="Chapter2___Overview">Overview</h2>'
                         '<p>Original prose.</p><section><h3 id="Chapter2___Overview___formalization">Formalization</h3>'
                         '<p>Declaration: MonoidAlgebra</p>'
                         '<p>Alignment metadata: book-ref=Chapter2/Overview/Derived4; role=supporting</p>'
                         '</section></section></main></html>')
        with self.assertRaisesRegex(ValueError, "expected one prose anchor"):
            prepare_document(document, {"Chapter2/Overview": [{"after": "Changed source."}]}, "a" * 40, {})


if __name__ == "__main__":
    unittest.main()
