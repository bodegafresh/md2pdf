from md2pdf.domain.ports.ai_provider import AiProvider


class SummarizerService:
    def __init__(self, ai: AiProvider):
        self.ai = ai


    def summary(self, text: str, words: int = 200, focus: str | None = None) -> str:
        return self.ai.summarize(text, words=words, focus=focus)


    def glossary(self, text: str, max_terms: int = 20) -> dict[str, str]:
        return self.ai.glossary(text, max_terms=max_terms)