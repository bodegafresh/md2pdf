import re, hashlib
from pathlib import Path
from md2pdf.domain.ports.diagram_engine import DiagramEngine


class DiagramService:
    MERMAID = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)
    PLANTUML = re.compile(r"```plantuml\n(.*?)```", re.DOTALL)


    def __init__(self, mermaid_engine: DiagramEngine | None, plantuml_engine: DiagramEngine | None):
        self.mermaid = mermaid_engine
        self.plantuml = plantuml_engine


    def process(self, md: str, assets_dir: str) -> str:
        assets = Path(assets_dir); assets.mkdir(parents=True, exist_ok=True)


        def rep_mermaid(m):
            code = m.group(1)
            name = hashlib.sha1(code.encode()).hexdigest() + ".svg"
            out = assets / name
            if self.mermaid:
                self.mermaid.render_mermaid(code, str(out))
            return f"![diagram]({out.as_posix()})"


        def rep_plantuml(m):
            code = m.group(1)
            name = hashlib.sha1(code.encode()).hexdigest() + ".svg"
            out = assets / name
            if self.plantuml:
                self.plantuml.render_plantuml(code, str(out))
            return f"![diagram]({out.as_posix()})"


            md = self.MERMAID.sub(rep_mermaid, md)
            md = self.PLANTUML.sub(rep_plantuml, md)
        return md