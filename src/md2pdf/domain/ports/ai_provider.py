from typing import Optional, Dict


class AiProvider:
    def rewrite(self, text: str, tone: str = "professional", locale: str = "es-CL") -> str:
        raise NotImplementedError


def summarize(self, text: str, words: int = 180, focus: Optional[str] = None) -> str:
    raise NotImplementedError


def glossary(self, text: str, max_terms: int = 20) -> Dict[str, str]:
    raise NotImplementedError