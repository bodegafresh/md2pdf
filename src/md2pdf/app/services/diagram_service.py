import re
from pathlib import Path


class DiagramService:
    def __init__(self, mermaid_engine):
        self.mermaid = mermaid_engine


    def process(self, md: str, assets_dir: str = ".md.assets") -> str:
        pattern = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)
        out_dir = Path(assets_dir)


        def repl(match):
            code = match.group(1).strip()
            img_path = self.mermaid.render_mermaid(code, out_dir)
            return f"![diagram]({img_path})"


        return pattern.sub(repl, md)