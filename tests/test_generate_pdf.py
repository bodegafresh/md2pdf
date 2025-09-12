from pathlib import Path
from md2pdf.interfaces.cli import _build_usecase
from md2pdf.app.usecases.generate_pdf import GeneratePdfRequest


def test_generate_pdf(tmp_path):
    md = tmp_path / "doc.md"
    md.write_text("# Hola\n\nTexto", encoding="utf-8")
    uc = _build_usecase()
    out = uc.execute(GeneratePdfRequest(md_path=str(md), out_dir=str(tmp_path)))
    assert Path(out).exists()