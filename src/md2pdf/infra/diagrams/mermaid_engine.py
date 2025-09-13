import subprocess
import hashlib
from pathlib import Path
from md2pdf.domain.ports.diagram_engine import DiagramEngine


class MermaidCliEngine(DiagramEngine):
    def render_mermaid(self, code: str, out_path: str) -> str:
        h = hashlib.sha256(code.encode()).hexdigest()[:10]
        out_file = Path(out_path) / f"mermaid_{h}.png"
        out_file.parent.mkdir(parents=True, exist_ok=True)


        tmp_file = out_file.with_suffix(".mmd")
        tmp_file.write_text(code, encoding="utf-8")


        subprocess.run(["mmdc", "-i", str(tmp_file), "-o", str(out_file)], check=True)
        return str(out_file)