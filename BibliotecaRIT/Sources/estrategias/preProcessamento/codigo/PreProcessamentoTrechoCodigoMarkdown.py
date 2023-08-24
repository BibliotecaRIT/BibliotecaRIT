from BibliotecaRIT.Sources.estrategias.preProcessamento.PreProcessamentoStrategy import PreProcessamentoStrategy
from BibliotecaRIT.Sources.enums.EnumTag import EnumTag
import re


class PreProcessamentoTrechoCodigoMarkdown(PreProcessamentoStrategy):
    _regExp = '```\s*([a-zA-Z]+)?(\r)?\n([\s\S]*?)(\r)?\n```'

    @classmethod
    def contem(cls, string: str) -> bool:
        return True if re.search(cls._regExp,string) is not None else False
    
    @staticmethod
    def getTag() -> EnumTag:
        return EnumTag.TRECHO_CODIGO

    @classmethod
    def remover(cls,string:str) -> str:
        return re.sub(cls._regExp,' ',string)

