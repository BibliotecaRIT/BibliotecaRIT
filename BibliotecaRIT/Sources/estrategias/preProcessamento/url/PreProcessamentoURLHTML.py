from BibliotecaRIT.Sources.estrategias.preProcessamento.PreProcessamentoStrategy import PreProcessamentoStrategy
from BibliotecaRIT.Sources.enums.EnumTag import EnumTag
import re

class PreProcessamentoURLHTML(PreProcessamentoStrategy):
    _regExp = "<a\s*[^>]*>([\s\S]*?)<\/a\s*>"

    @classmethod
    def contem(cls, string: str) -> bool:
        return True if re.search(cls._regExp,string) is not None else False

    @staticmethod
    def getTag() -> EnumTag:
        return EnumTag.LINK

    @classmethod
    def remover(cls,string:str) -> str:
        match = re.search(cls._regExp,string)
        try:
            return re.sub(cls._regExp,match.groups()[0],string)
        except Exception as e:
            return re.sub(cls._regExp,re.escape(match.groups()[0]),string)
        


