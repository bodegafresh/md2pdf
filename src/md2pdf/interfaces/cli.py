import typer

from md2pdf.infra.parsers.markdownit_parser import MarkdownItParser
from md2pdf.infra.storage.local_fs_repo import LocalFsRepo
from md2pdf.infra.renderers.pdf_renderer import WeasyPrintRenderer
from md2pdf.infra.diagrams.mermaid_engine import MermaidCliEngine
from md2pdf.app.services.diagram_service import DiagramService
from md2pdf.app.services.chart_service import ChartService
from md2pdf.app.services.grammar_service import GrammarService
from md2pdf.app.services.summarizer_service import SummarizerService
from md2pdf.infra.ai.openai_provider import DummyOpenAiProvider
from md2pdf.infra.charts.matplotlib_engine import MatplotlibEngine
from md2pdf.app.usecases.generate_pdf import GeneratePdf, GeneratePdfRequest

app = typer.Typer(help="md2pdf CLI")


def _build_usecase() -> GeneratePdf:
    """
    Construye el caso de uso principal con los adaptadores por defecto.
    - Diagramas: Mermaid CLI (mmdc).
    - Charts: Matplotlib.
    - PDF: WeasyPrint.
    - IA: Dummy (placeholder seguro/offline).
    """
    mdp = MarkdownItParser()
    storage = LocalFsRepo()
    pdf = WeasyPrintRenderer()

    mer_engine = MermaidCliEngine()
    # OJO: DiagramService en tu repo actual acepta SOLO 1 parámetro (mermaid_engine)
    diag = DiagramService(mer_engine)

    charts = ChartService(MatplotlibEngine())
    grammar = GrammarService(enabled=False)
    ai = DummyOpenAiProvider()
    summarizer = SummarizerService(ai)

    # Firma actual de GeneratePdf:
    # (md_parser, storage, pdf_renderer, diagram_svc, chart_svc, grammar_svc, summarizer_svc)
    return GeneratePdf(mdp, storage, pdf, diag, charts, grammar, summarizer)


@app.command()
def generate(
    infile: str = typer.Option(..., "--in", help="Ruta al archivo .md"),
    theme: str = typer.Option("default", "--theme"),
    out_dir: str = typer.Option("output", "--out-dir"),
    include_summary: bool = typer.Option(True, "--include-summary"),
    include_glossary: bool = typer.Option(True, "--include-glossary"),
):
    """
    Genera un PDF desde Markdown aplicando tema, diagramas y gráficos.
    """
    uc = _build_usecase()
    pdf_path = uc.execute(
        GeneratePdfRequest(
            md_path=infile,
            theme_name=theme,
            include_summary=include_summary,
            include_glossary=include_glossary,
            out_dir=out_dir,
        )
    )
    typer.echo(pdf_path)


@app.command()
def preview(
    infile: str = typer.Option(..., "--in", help="Ruta al archivo .md"),
    theme: str = typer.Option("default", "--theme"),
):
    """
    Renderiza el HTML final (útil para depurar temas) y lo imprime por stdout.
    """
    from md2pdf.infra.renderers.html_renderer import HtmlRenderer

    mdp = MarkdownItParser()
    storage = LocalFsRepo()
    renderer = HtmlRenderer()

    raw = storage.load_markdown(infile)
    meta, md = mdp.split_front_matter(raw)
    html = renderer.render(mdp.to_html(md), theme=theme, branding=None, meta=meta)
    print(html)


if __name__ == "__main__":
    app()
