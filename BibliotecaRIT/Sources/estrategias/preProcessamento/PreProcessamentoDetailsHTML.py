from BibliotecaRIT.Sources.estrategias.preProcessamento.PreProcessamentoStrategy import PreProcessamentoStrategy
from BibliotecaRIT.Sources.enums.EnumTag import EnumTag
import re


class PreProcessamentoDetailsHTML(PreProcessamentoStrategy):
    _regExp = '<details>'
                         
    @classmethod
    def contem(cls, string: str) -> bool:
        return True if re.search(cls._regExp,string) is not None else False

    @staticmethod
    def getTag() -> EnumTag:
        return EnumTag.TRECHO_CODIGO

    @classmethod
    def remover(cls,string:str) -> str:
        tupla = string.rpartition('<details>')
        tupla2= string.rpartition('</details>')
        string = tupla[0] + tupla2[2]
        return string
