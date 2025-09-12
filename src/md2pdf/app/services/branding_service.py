import yaml
from pathlib import Path
from md2pdf.domain.entities import Branding


class BrandingService:
    def __init__(self, themes_dir: str = "themes"):
        self.themes_dir = Path(themes_dir)


    def get(self, name: str, overrides: dict | None = None) -> Branding:
        theme = self.themes_dir / name / "theme.yaml"
        data = yaml.safe_load(theme.read_text(encoding="utf-8"))
        if overrides:
            data.update(overrides)
        return Branding(name=name, colors=data.get("colors", {}), fonts=data.get("fonts", {}), logo_path=data.get("logo"))