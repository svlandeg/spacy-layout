<a href="https://explosion.ai"><img src="https://explosion.ai/assets/img/logo.svg" width="125" height="125" align="right" /></a>

# spaCy Layout: Process PDFs, Word documents and more with spaCy

This plugin integrates with [Docling](https://ds4sd.github.io/docling/) to bring structured processing of **PDFs**, **Word documents** and other input formats to your [spaCy](https://spacy.io) pipeline. It outputs clean, **structured data** in a text-based format and outputs spaCy's familiar [`Doc`](https://spacy.io/api/doc) objects that let you accessed labelled text spans like setions, headings, or footnotes.

This also makes it easy to apply powerful NLP techniques to your documents, including linguistic analysis, named entity recognition, text classification and more. The plugin also includes [Prodigy](https://prodi.gy) recipes for annotating the converted documents.

## 📝 Usage

```python
import spacy
from spacy_layout import spaCyLayout

nlp = spacy.blank("en")
layout = spaCyLayout(nlp)

# Process a document and create a spaCy Doc object
doc = layout("./starcraft.pdf")

# The text-based contents of the document
print(doc.text)
# Document layout including pages and page sizes
print(doc._.layout)

# Layout spans for different sections
for span in doc.spans["layout"]:
    # Document section and token and character offsets into the text
    print(span.text, span.start, span.end, span.start_char, span.end_char)
    # Section type, e.g. "text", "title", "section_header" etc.
    print(span.label_)
    # Layout features of the section, including bounding box
    print(span._.layout)
```

## 🎛️ API

### Data and extension attributes

```python
layout = spaCyLayout(nlp)
doc = layout("./starcraft.pdf")
print(doc._.layout)
for span in doc.spans["layout"]:
    print(span.label_, span._.layout)
```

| Attribute | Type | Description |
| --- | --- | --- |
| `Span.label_` | `str` | The type of the extracted layout span, e.g. `"text"` or `"section_header"`. [See here](https://github.com/DS4SD/docling-core/blob/main/docling_core/types/doc/labels.py) for options.
| `Span._.layout` | `SpanLayout` | Layout features of a layout span. |
| `Doc._.layout` | `DocLayout` | Layout features of the document. |
| `Doc._.pages` | `list[tuple[PageLayout, list[Span]]]` | Pages in the document and the spans they contain. |

### <kbd>dataclass</kbd> PageLayout

| Attribute | Type | Description |
| --- | --- | --- |
| `page_no` | `int` | The page number (1-indexed). |
| `width` | `float` | Page with in pixels. |
| `height` | `float` | Page height in pixels. |

### <kbd>dataclass</kbd> DocLayout

| Attribute | Type | Description |
| --- | --- | --- |
| pages | `list[PageLayout]` | The pages in the document. |

### <kbd>dataclass</kbd> SpanLayout

| Attribute | Type | Description |
| --- | --- | --- |
| `x` | `float` | Horizontal offset of the bounding box in pixels. |
| `y` | `float` | Vertical offset of the bounding box in pixels. |
| `width` | `float` | Width of the bounding box in pixels. |
| `height` | `float` | Height of the bounding box in pixels. |
| `page_no` | `int` | Number of page the span is on. |

### <kbd>class</kbd> `spaCyLayout`

#### <kbd>method</kbd> `spaCyLayout.__init__`

Initialize the document processor.

```python
nlp = spacy.blank("en")
layout = spaCyLayout(nlp)
```

| Argument | Type | Description |
| --- | --- | --- |
| `nlp` | `spacy.language.Language` | The initialized `nlp` object to use for tokenization. |
| `separator` | `str` | Token used to separate sections in the created `Doc` object. The separator won't be part of the layout span. If `None`, no separator will be added. Defaults to `"\n\n"`. |
| `attrs` | `dict[str, str]` | Override the custom spaCy attributes. Can include `"doc_layout"`, `"doc_pages"`, `"span_layout"` and `"span_group"`. |
| `docling_options` | `dict[InputFormat, FormatOption]` | [Format options](https://ds4sd.github.io/docling/usage/#advanced-options) passed to Docling's `DocumentConverter`. |
| **RETURNS** | `spaCyLayout` | The initialized object. |

#### <kbd>method</kbd> `spaCyLayout.__call__`

Process a document and create a spaCy [`Doc`](https://spacy.io/api/doc) object containing the text content and layout spans, available via `Doc.spans["layout"]` by default.

```python
layout = spaCyLayout(nlp)
doc = layout("./starcraft.pdf")
```

| Argument | Type | Description |
| --- | --- | --- |
| `path` | `str` / `Path` | Path to document to process. |
| **RETURNS** | `Doc` | The processed spaCy `Doc` object. |

## ✨ Prodigy Recipes

The package includes [Prodigy](https://prodi.gy) recipes for annotating the extracted data in a convenient text-based way, e.g. to add named entities and other span annotations or assign categories to the documents. You can also  use `spacy-layout` in your own [custom recipes](https://prodi.gy/docs/custom-recipes) to support PDFs and other documents as input to Prodigy. For more PDF workflows, see the [Prodigy-PDF](https://prodi.gy/plugins#pdf) plugin.

> ⚠ **Coming soon**
