import matplotlib.pyplot as plt
import yaml
import hashlib
from pathlib import Path


class MatplotlibEngine:
    def render_chart(self, block: str, out_path: str) -> str:
        spec = yaml.safe_load(block)
        title = spec.get("title", "Chart")
        ctype = spec.get("type", "bar")
        labels = spec.get("data", {}).get("labels", [])
        series = spec.get("data", {}).get("series", [])


        h = hashlib.sha256(block.encode()).hexdigest()[:10]
        out_file = Path(out_path) / f"chart_{h}.png"
        out_file.parent.mkdir(parents=True, exist_ok=True)


        fig, ax = plt.subplots()
        if ctype == "bar":
            for s in series:
                ax.bar(labels, s.get("values", []), label=s.get("name"))
        elif ctype == "line":
            for s in series:
                ax.plot(labels, s.get("values", []), label=s.get("name"))
        elif ctype == "pie" and series:
            ax.pie(series[0].get("values", []), labels=labels)


        ax.set_title(title)
        if series and ctype != "pie":
            ax.legend()


        fig.savefig(out_file)
        plt.close(fig)
        return str(out_file)