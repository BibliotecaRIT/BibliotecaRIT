from BibliotecaRIT.Sources.estrategias.preProcessamento.PreProcessamentoStrategy import PreProcessamentoStrategy
from BibliotecaRIT.Sources.enums.EnumTag import EnumTag
import re

class PreProcessamentoURL(PreProcessamentoStrategy):
    _regExp = "http(s?):\/\/[^\s]+[\s]?(\))?"

    @classmethod
    def contem(cls, string: str) -> bool:
        return True if re.search(cls._regExp,string) is not None else False

    @staticmethod
    def getTag() -> EnumTag:
        return EnumTag.LINK

    @classmethod
    def remover(cls,string:str) -> str:
        return re.sub(cls._regExp," ",string)


