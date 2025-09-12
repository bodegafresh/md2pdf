from typing import Tuple


class StorageRepo:
    def load_markdown(self, path: str) -> str:
        raise NotImplementedError


def build_output_path(self, out_dir: str, meta: dict) -> str:
    raise NotImplementedError