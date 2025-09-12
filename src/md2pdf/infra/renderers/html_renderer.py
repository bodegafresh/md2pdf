
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path
import yaml


class HtmlRenderer:
    def __init__(self, themes_dir: str = "themes"):
        self.themes_dir = Path(themes_dir)
        self.env = Environment(
            loader=FileSystemLoader(str(self.themes_dir)),
            autoescape=select_autoescape()
        )


    def _load_theme(self, name: str, overrides: dict | None = None) -> dict:
        theme_dir = self.themes_dir / name
        data = yaml.safe_load((theme_dir / "theme.yaml").read_text(encoding="utf-8"))
        if overrides:
            data.update(overrides)
        data["_dir"] = str(theme_dir)
        return data


    def render(self, body_html: str, theme: str, branding: dict | None, meta: dict) -> str:
        theme_data = self._load_theme(theme, branding)
        template = self.env.get_template(f"{theme}/base.html.j2")
        return template.render(body=body_html, meta=meta, theme=theme_data)