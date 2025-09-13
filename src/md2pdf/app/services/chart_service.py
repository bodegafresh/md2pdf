import re
from pathlib import Path


class ChartService:
    def __init__(self, chart_engine):
        self.chart_engine = chart_engine

    def process(self, md: str, assets_dir: str = ".md.assets") -> str:
        pattern = re.compile(r"```chart\n(.*?)```", re.DOTALL)
        out_dir = Path(assets_dir)

        def repl(match):
            block = match.group(1).strip()
            img_path = self.chart_engine.render_chart(block, out_dir)
            return f"![chart]({img_path})"

        return pattern.sub(repl, md)