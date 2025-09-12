import io, base64
from pathlib import Path
import matplotlib.pyplot as plt


class MatplotlibEngine:
    def render_chart(self, spec: dict, out_path: str) -> str:
        kind = spec.get("type", "bar")
        title = spec.get("title", "")
        data = spec.get("data", {})
        labels = data.get("labels", [])
        series = data.get("series", [])


        plt.figure()
        if kind == "bar":
            for s in series:
                plt.bar(labels, s.get("values", []))
        elif kind == "line":
            for s in series:
                plt.plot(labels, s.get("values", []))
        elif kind == "pie":
            if series:
                plt.pie(series[0].get("values", []), labels=labels)
        plt.title(title)
        out = Path(out_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(out)
        plt.close()
        return str(out)