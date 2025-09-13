from md2pdf.infra.parsers.markdownit_parser import MarkdownItParser


def test_front_matter_split():
    text = """---\ncliente: X\n---\n# Titulo\nBody"""
    fm, body = MarkdownItParser().split_front_matter(text)
    assert fm["cliente"] == "X"
    assert "Titulo" in body