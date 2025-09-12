from weasyprint import HTML, CSS
from pathlib import Path


from md2pdf.domain.ports.renderer_pdf import PdfRenderer


class WeasyPrintRenderer(PdfRenderer):
    def html_to_pdf(self, html: str, assets_dir: str, out_path: str) -> str:
        out = Path(out_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        HTML(string=html, base_url=str(Path(assets_dir).resolve())).write_pdf(str(out))
        return str(out)