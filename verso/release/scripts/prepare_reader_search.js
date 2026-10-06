/* Rebuild Verso's full-text index from its retained book sections. */
const fs = require("node:fs");
const path = require("node:path");
const crypto = require("node:crypto");
const root = process.argv[2];
const elasticlunr = require(path.join(root, "elasticlunr.min.js"));
// Indexing and browser queries must tokenize typographic dashes identically.
// Otherwise “Schur–Weyl” is one token while “Schur Weyl” is two.
const wordSeparators = "[\\s\\-\\u2010-\\u2015\\u2212]+";
elasticlunr.tokenizer.setSeperator(new RegExp(wordSeparators));
const docs = new Map();
const xref = JSON.parse(fs.readFileSync(path.join(root, "../xref.json"), "utf8"));
const scanPages = new Set(Object.values(xref["Verso.Genre.Manual.section"]?.contents || {})
  .flat().filter(entry => entry.data?.readerScanMarker).map(entry => entry.address));
const technical = new Set(["Formalization", "Primary declarations", "Supporting declarations"]);
const citation = /\* Etingof et al\., Introduction to Representation Theory \[book-ref=[^\]]+\]/g;
for (const file of fs.readdirSync(root)) {
  if (!/^searchIndex_\d+\.[a-z0-9]+\.js$/.test(file)) continue;
  const text = fs.readFileSync(path.join(root, file), "utf8");
  const bucket = JSON.parse(text.slice(text.indexOf("resolve(") + 8, text.lastIndexOf(");")));
  for (const doc of Object.values(bucket)) {
    if (scanPages.has(doc.id.split("#")[0])) continue;
    if (technical.has(doc.header) || /(?:^|\t)Formalization(?:\t|$)/.test(doc.context)) continue;
    doc.contents = doc.contents.replace(citation, "");
    const context = doc.context.split("\t");
    doc.context = context.filter((value, i) => !i || value !== context[i - 1]).join("\t");
    const key = doc.id.split("#")[0] + "\t" + doc.header;
    if (!docs.has(key) || docs.get(key).contents.length < doc.contents.length) docs.set(key, doc);
  }
}
const index = elasticlunr(function () {
  this.setRef("id");
  this.addField("header");
  this.addField("contents");
  this.addField("id");
  this.saveDocument(false);
});
const buckets = Array.from({length: 256}, () => ({}));
for (const doc of docs.values()) {
  index.addDoc(doc);
  const bucket = [...Buffer.from(doc.id, "utf8")].reduce((sum, value) => (sum + value) % 256, 0);
  buckets[bucket][doc.id] = doc;
}
const serialized = JSON.stringify(index.toJSON());
const version = crypto.createHash("sha256").update(serialized).digest("hex").slice(0, 16);
fs.writeFileSync(path.join(root, "searchIndex.js"),
  `elasticlunr.tokenizer.setSeperator(new RegExp(${JSON.stringify(wordSeparators)}));\n` +
  `const __verso_searchIndexData = ${serialized};\n` +
  `window.searchIndex = elasticlunr.Index.load(__verso_searchIndexData);\n` +
  `window.docContents = {};\nwindow.docPriorities = {};\nwindow.searchIndexVersion = ${JSON.stringify(version)};\n`);
for (let number = 0; number < 256; number++) {
  fs.writeFileSync(path.join(root, `searchIndex_${number}.${version}.js`),
    `window.docContents[${number}].resolve(${JSON.stringify(buckets[number])});\n`);
}
const mapper = path.join(root, "domain-mappers.js");
const text = fs.readFileSync(mapper, "utf8");
const start = text.indexOf("const Verso_DOT_Genre_DOT_Manual_DOT_section =");
const prefix = text.slice(0, start);
const section = text.slice(start);
if (!section.includes("Object.entries(domainData.contents).map(")) throw Error("section search mapper changed");
fs.writeFileSync(mapper, prefix + section.replace("Object.entries(domainData.contents).map(",
  "Object.entries(domainData.contents).filter(([, value]) => !value[0].data.readerHidden).map("));
console.log(JSON.stringify({search_documents: docs.size, search_version: version}));
