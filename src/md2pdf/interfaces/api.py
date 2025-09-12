from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse
from io import BytesIO
from md2pdf.interfaces.cli import _build_usecase
from md2pdf.infra.parsers.markdownit_parser import MarkdownItParser
from md2pdf.infra.renderers.html_renderer import HtmlRenderer


app = FastAPI(title="md2pdf API")


@app.get("/themes")
def themes():
    return ["default", "kolff"]


@app.post("/preview", response_class=HTMLResponse)
async def preview(md: str = Form(...), theme: str = Form("default")):
    parser = MarkdownItParser(); renderer = HtmlRenderer()
    meta, body = parser.split_front_matter(md)
    return renderer.render(parser.to_html(body), theme=theme, branding=None, meta=meta)


@app.post("/render")
async def render(md: UploadFile, theme: str = Form("default")):
    uc = _build_usecase()
    # Guardar a temp y ejecutar caso de uso
    import tempfile, shutil
    with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as f:
        shutil.copyfileobj(md.file, f)
        temp = f.name
    path = uc.execute(type("Req", (), {"md_path": temp, "theme_name": theme, "branding_overrides": None,
                                        "enable_ai_polish": False, "include_summary": True,
                                        "include_glossary": True, "out_dir": "/tmp"})())
    return JSONResponse({"pdf_path": path})