import subprocess, tempfile, hashlib
from pathlib import Path
from md2pdf.domain.ports.diagram_engine import DiagramEngine


class MermaidCliEngine(DiagramEngine):
    def render_mermaid(self, code: str, out_path: str) -> str:
        out = Path(out_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile("w", suffix=".mmd", delete=False) as f:
            f.write(code)
            tmp = f.name
        subprocess.run(["mmdc", "-i", tmp, "-o", str(out)], check=True)
        return str(out)


    def render_plantuml(self, code: str, out_path: str) -> str:
        raise NotImplementedError