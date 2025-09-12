from dataclasses import dataclass
from md2pdf.domain.ports.ai_provider import AiProvider


@dataclass
class ImproveWritingRequest:
    text: str
    tone: str = "professional"
    locale: str = "es-CL"


class ImproveWriting:
    def __init__(self, ai: AiProvider):
        self.ai = ai


    def execute(self, req: ImproveWritingRequest) -> str:
        return self.ai.rewrite(req.text, tone=req.tone, locale=req.locale)                          