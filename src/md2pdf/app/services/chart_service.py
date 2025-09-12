import re, hashlib, yaml
from pathlib import Path
from md2pdf.infra.charts.matplotlib_engine import MatplotlibEngine


class ChartService:
    CHART = re.compile(r"```chart\n(.*?)```", re.DOTALL)


    def __init__(self, engine: MatplotlibEngine | None = None):
        self.engine = engine or MatplotlibEngine()


    def process(self, md: str, assets_dir: str) -> str:
        assets = Path(assets_dir); assets.mkdir(parents=True, exist_ok=True)


        def rep(m):
            spec = yaml.safe_load(m.group(1)) or {}
            name = hashlib.sha1(str(spec).encode()).hexdigest() + ".png"
            out = assets / name
            self.engine.render_chart(spec, str(out))
            return f"![chart]({out.as_posix()})"


        return self.CHART.sub(rep, md)