import language_tool_python


class LanguageToolProvider:
    def __init__(self, lang: str = "es"):
        self.tool = language_tool_python.LanguageToolPublicAPI(lang)


    def correct(self, text: str) -> str:
        return self.tool.correct(text)