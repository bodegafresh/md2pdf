from typing import Tuple, Dict


class MarkdownParser:
    def split_front_matter(self, text: str) -> tuple[dict, str]:
        raise NotImplementedError


def to_html(self, markdown: str) -> str:
    raise NotImplementedError