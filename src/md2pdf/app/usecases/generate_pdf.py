from dataclasses import dataclass
from pathlib import Path
from md2pdf.domain.ports.markdown_parser import MarkdownParser
from md2pdf.domain.ports.renderer_pdf import PdfRenderer
from md2pdf.domain.ports.storage_repo import StorageRepo
from md2pdf.app.services.diagram_service import DiagramService
from md2pdf.app.services.chart_service import ChartService
from md2pdf.app.services.grammar_service import GrammarService
from md2pdf.app.services.summarizer_service import SummarizerService
from md2pdf.infra.renderers.html_renderer import HtmlRenderer


@dataclass
class GeneratePdfRequest:
    md_path: str
    theme_name: str = "default"
    branding_overrides: dict | None = None
    enable_ai_polish: bool = False
    include_summary: bool = True
    include_glossary: bool = True
    out_dir: str = "output"


class GeneratePdf:
    def __init__(self, md_parser: MarkdownParser, storage: StorageRepo, pdf_renderer: PdfRenderer,
        diagram_svc: DiagramService, chart_svc: ChartService,
        grammar_svc: GrammarService, summarizer_svc: SummarizerService | None):
        self.md_parser = md_parser
        self.storage = storage
        self.pdf_renderer = pdf_renderer
        self.diagram_svc = diagram_svc
        self.chart_svc = chart_svc
        self.grammar_svc = grammar_svc
        self.summarizer_svc = summarizer_svc
        self.html_renderer = HtmlRenderer()


    def execute(self, req: GeneratePdfRequest) -> str:
        raw = self.storage.load_markdown(req.md_path)
        meta, md = self.md_parser.split_front_matter(raw)


        assets_dir = Path(req.md_path).with_suffix("") # ./examples/cotizacion_kolff
        assets_dir = f"{assets_dir}.assets"


        md = self.diagram_svc.process(md, assets_dir)
        md = self.chart_svc.process(md, assets_dir)


        md = self.grammar_svc.correct(md)


        if self.summarizer_svc and req.include_summary:
            summary = self.summarizer_svc.summary(md, words=200, focus=meta.get("focus"))
            md += f"\n\n## Resumen ejecutivo\n\n{summary}\n"


        if self.summarizer_svc and req.include_glossary:
            terms = self.summarizer_svc.glossary(md, max_terms=20)
            if terms:
                md += "\n\n## Glosario\n\n" + "\n".join(f"- **{k}**: {v}" for k, v in terms.items())


        body_html = self.md_parser.to_html(md)
        html = self.html_renderer.render(body_html, theme=req.theme_name, branding=req.branding_overrides, meta=meta)


        out_path = self.storage.build_output_path(req.out_dir, meta)
        return self.pdf_renderer.html_to_pdf(html, assets_dir="themes", out_path=out_path)