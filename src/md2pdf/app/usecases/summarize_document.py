from dataclasses import dataclass
from md2pdf.app.services.summarizer_service import SummarizerService


@dataclass
class SummarizeRequest:
    text: str
    words: int = 200


class SummarizeDocument:
    def __init__(self, svc: SummarizerService):
        self.svc = svc


    def execute(self, req: SummarizeRequest) -> str:
        return self.svc.summary(req.text, words=req.words)