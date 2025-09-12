from pathlib import Path
from datetime import date
from md2pdf.domain.ports.storage_repo import StorageRepo


class LocalFsRepo(StorageRepo):
    def load_markdown(self, path: str) -> str:
        return Path(path).read_text(encoding="utf-8")


    def build_output_path(self, out_dir: str, meta: dict) -> str:
        cliente = meta.get("cliente", "_generic").lower().replace(" ", "_")
        fecha = str(meta.get("fecha", date.today()))
        slug = meta.get("proyecto", meta.get("title", "documento")).lower().replace(" ", "-")
        out = Path(out_dir) / cliente / f"{fecha}_{slug}.pdf"
        return str(out)