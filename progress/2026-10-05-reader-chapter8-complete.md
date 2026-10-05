# Chapter 8: homological algebra

Verified local checkpoint: 542/583 reviewed, 831 explanations, 41 pending.
All twenty-four Chapter 8 items (orders 523–546) now have reading decisions.
This is a local reading-pass checkpoint, not publication or goal completion.

## Reading changes

Add thirty-four explanations and fifty-seven expandable checked statements.
Replace twenty-four titles with mathematical headings, and make nine joins:
projectivity with its theorem and definition; injectivity with its theorem,
definition and duality example; categorical projectivity/injectivity with
the Hom definition; the Tor/Ext introduction with resolutions and their
existence; enough projectives with the counterexamples and finite free covers.

Explain lifting and splitting, the free-retract formulation, exact Hom,
right modules encoded by opposite rings, balanced tensors over arbitrary
rings, projective versus flat localization, the pushout proof of injectivity,
double-dual restrictions, chain versus cochain indexing, augmentation and
quasi-isomorphism data, free covers of successive kernels, variance of Ext,
homotopy independence, degree-zero comparisons, the extension-cocycle bridge,
connecting maps, balancing and horseshoe resolutions. The cyclic calculations
distinguish finitely generated modules from finite groups or finite-dimensional
vector spaces. Each of the five Koszul questions has its own relevant note.

Replace forty-three vague docstrings in twenty-one generating formalization
modules with mathematical descriptions. No declaration names, types, proofs,
alignment roles, linter settings, visibility or protections are changed.

## Honest scope and layout

The projective/injective duality equivalence assumes both the algebra and the
module finite-dimensional over the field; the unrestricted forward direction
is distinguished from the checked restricted converse. The tensor-product Ext
formula assumes finite-dimensional algebras and first-argument modules as well
as the coefficient modules; it does not certify the book's full printed scope.
Both restrictions are explicit status notes and comparison records.

The general categorical Ext interface and projective-resolution comparison
are linked separately from the field-linear Hom-complex interface. For Tor,
explain the required right first argument where the book prints left modules.
Enough projectives does not by itself give an arbitrary abelian category a
tensor product. The dual-tensor counterexample is not presented as a disproof
of the printed Ext formula.

In both packets and native source, separate injectivity conditions (ii)/(iii)
and the comparison-map definition from question (ii). Remove only the trailing
scan marker “[Blank page]” from the Koszul exercise. Immutable original files
and corpus hashes remain unchanged.

The visual pass catches a Tor explanation interrupting “Similarly,” before
the Ext display. Move it to the Tor display and add both a source regression
and a browser reading-order assertion. Do not interrupt that original
transition. The chapter introduction's paragraph now shares its readable
heading; confirm the paragraph on the old published nested body-heading page.

## Verification

- Read all twenty-four native passages. Review records specify the actual
  generating interfaces/proof portions compared; imported construction engines
  remain dependencies, not a claimed audit of the whole transitive library.
- Capture twenty-six published routes and 186 anchors, including two nested
  chapter-heading URLs. Resolve actual public xref addresses, not guessed slugs.
  Extend saved-bookmark selection to a selected item's body-heading aliases.
- All twenty-four native modules exactly preserve their previous contents
  except titles and the three declared layout repairs. Fresh assembly in
  /tmp/etingof-reader-chapter8-assembly-RaaEJp reproduces their decoded titles
  and book bodies. Avoid unescaped square brackets in the polynomial title.
- Compare all twenty-four passages across fifteen reading pages with the
  preceding prepared DOM, allowing only the stated paragraph/scan repairs.
  For the introduction, recover its unchanged paragraph from the prior nested
  heading and the complete native source; do not treat an empty wrapper as
  evidence that the chapter had no prose.
- Official build session 39655 exits zero; after the placement and legacy-route
  fixes, final build session 83689 also exits zero. All 20,771 jobs pass,
  2,436 alignment rows have no panel drift, and reader validation has zero errors.
  Final preparation has 831 notes, fourteen footnotes, seventy-eight joins,
  440 redirects and 351 legacy-title redirects.
- Eighty-one reader/preparation tests (39 + 42) and ten immutable-source gate
  tests pass. Private-source exactness passes. Original-text integrity verifies
  all 583 hashes, 235 pages and 5,716 lines, without errors, overlaps or gaps.
- Search version 45bdce147c19f36d has 788 documents. All twenty-four revised
  passage titles have one matching reading document and rank first; the
  introduction's canonical content document uses its retained heading-2 tag.
- Initial browser session 86545 passes eighteen pages. Final session 53172
  passes eighteen pages, 31 reviewed reading items, 24 annotated items,
  72 collapsed/expanded cases, 32 definition bookmarks, 308 card actions,
  24 helper links, 32 legacy routes and 470 saved-bookmark cases. No JavaScript
  errors or desktop/mobile overflow. Include Chapter 1's multiparagraph note,
  Chapter 6's Sylvester note, and Chapter 7's main cohomology/footnote regression.
- Inspect phone projectivity and Koszul pages and the desktop tensor-algebra
  page, including the corrected placement. Screenshots are under
  verso/release/_out/reader-chapter8-{projectivity,injectivity,exact-sequences,
  tensor-algebras,koszul}-{1440,390}.png. Scoped whitespace checks pass.

## Remaining work

Next: thirty-five Chapter 9 items; four front-matter and two bibliography items
remain. Their native sources were read as preparation, not yet marked reviewed.
The historical bibliography has merged adjacent citation paragraphs to repair
in its generation inputs. Complete global navigation/thin-wrapper polishing,
publication through the generating repositories, and public live-site checks.

Read-only publication check still finds source PR #4 open, REVIEW_REQUIRED and
BLOCKED, head f9c69bafeccd5158a7249449a92446f844dac381, no merge commit.
No remote writes or approval changes in this batch. Do not bypass the source
review or publish an unmerged materialization. The local source-link structure
is verified, but new lines and public proof destinations require the actual
merged source pin and live checks after materialization.
