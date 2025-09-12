class DiagramEngine:
    def render_mermaid(self, code: str, out_path: str) -> str:
        raise NotImplementedError


def render_plantuml(self, code: str, out_path: str) -> str:
    raise NotImplementedError