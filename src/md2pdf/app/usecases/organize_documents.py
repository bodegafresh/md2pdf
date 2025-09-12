from pathlib import Path
from typing import Iterable


class OrganizeDocuments:
    def scan(self, root: str) -> Iterable[str]:
        for p in Path(root).rglob("*.md"):
            yield str(p)