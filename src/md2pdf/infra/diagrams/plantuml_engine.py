import subprocess, tempfile
from pathlib import Path
from md2pdf.domain.ports.diagram_engine import DiagramEngine


class PlantUmlCliEngine(DiagramEngine):
    def render_mermaid(self, code: str, out_path: str) -> str:
        raise NotImplementedError


    def render_plantuml(self, code: str, out_path: str) -> str:
        out = Path(out_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile("w", suffix=".puml", delete=False) as f:
            f.write(code)
            tmp = f.name
        subprocess.run(["java", "-jar", "/usr/share/plantuml/plantuml.jar", "-tsvg", tmp, "-o", str(out.parent)], check=True)
        # PlantUML genera en mismo dir con mismo nombre .svg
        gen = Path(tmp).with_suffix(".svg")
        gen.rename(out)
        return str(out)