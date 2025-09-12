try:
    from md2pdf.infra.ai.langtool_provider import LanguageToolProvider
except Exception: # pragma: no cover
    LanguageToolProvider = None


class GrammarService:
    def __init__(self, enabled: bool = False, lang: str = "es"):
        self.enabled = enabled and LanguageToolProvider is not None
        self.provider = LanguageToolProvider(lang) if self.enabled else None


    def correct(self, text: str) -> str:
        if not self.provider:
            return text
        return self.provider.correct(text)