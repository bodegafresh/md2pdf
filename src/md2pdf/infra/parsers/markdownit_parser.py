from markdown_it import MarkdownIt
from mdit_py_plugins.anchors import anchors_plugin
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.tasklists import tasklists_plugin
import yaml
from typing import Tuple


from md2pdf.domain.ports.markdown_parser import MarkdownParser


class MarkdownItParser(MarkdownParser):
    def __init__(self) -> None:
        self.md = (
            MarkdownIt("commonmark", {"html": True})
            .use(anchors_plugin)
            .use(tasklists_plugin)
            .use(front_matter_plugin)
        )


    def split_front_matter(self, text: str) -> tuple[dict, str]:
        if text.startswith("---\n"):
            end = text.find("\n---\n", 4)
            if end != -1:
                fm = yaml.safe_load(text[4:end]) or {}
                body = text[end + 5 :]
                return fm, body
        return {}, text


    def to_html(self, markdown: str) -> str:
        return self.md.render(markdown)