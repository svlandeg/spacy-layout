from pathlib import Path

import pytest
import spacy
from docling_core.types.doc.labels import DocItemLabel

from spacy_layout import spaCyLayout
from spacy_layout.types import DocLayout, SpanLayout


@pytest.fixture
def pdf_path():
    return Path(__file__).parent / "data" / "starcraft.pdf"


@pytest.fixture
def nlp():
    return spacy.blank("en")


@pytest.fixture
def span_labels():
    return [label.value for label in DocItemLabel]


def test_general(nlp, pdf_path, span_labels):
    layout = spaCyLayout(nlp)
    doc = layout(pdf_path)
    assert isinstance(doc._.get(layout.attrs.doc_layout), DocLayout)
    for span in doc.spans[layout.attrs.span_group]:
        assert span.text
        assert span.label_ in span_labels
        assert isinstance(span._.get(layout.attrs.span_layout), SpanLayout)
