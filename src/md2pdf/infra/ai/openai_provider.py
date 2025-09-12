from md2pdf.domain.ports.ai_provider import AiProvider


class DummyOpenAiProvider(AiProvider):
    """Adaptador de ejemplo: maqueta reescritura/resumen/glosario.
    Reemplaza por tu LLM preferido. Mantiene fenced code intacto por simplicidad.
    """
    def rewrite(self, text: str, tone: str = "professional", locale: str = "es-CL") -> str:
        return text # No-op en MVP (seguro y offline)


    def summarize(self, text: str, words: int = 180, focus: str | None = None) -> str:
        head = text.strip().splitlines()[:20]
        return ("Resumen (MVP offline):\n" + "\n".join(head))[:words*7]


    def glossary(self, text: str, max_terms: int = 20) -> dict[str, str]:
        return {}