class LanguageMode:
    def __init__(self, language):
        self._languageMode = language

    @property
    def languageMode(self):
        return self._languageMode

    @languageMode.setter
    def languageMode(self, value):
        self._languageMode = value


    