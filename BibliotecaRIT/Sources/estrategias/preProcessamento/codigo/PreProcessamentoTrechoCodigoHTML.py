from BibliotecaRIT.Sources.estrategias.preProcessamento.PreProcessamentoStrategy import PreProcessamentoStrategy
from BibliotecaRIT.Sources.enums.EnumTag import EnumTag
import re


class PreProcessamentoTrechoCodigoHTML(PreProcessamentoStrategy):
    _regExp ='<pre><code>(.*?)<\/code><\/pre>'
    _flags = re.DOTALL
    @classmethod
    def contem(cls, string: str) -> bool:
        return True if re.search(cls._regExp,string,flags=cls._flags) is not None else False
    @staticmethod
    def getTag() -> EnumTag:
        return EnumTag.TRECHO_CODIGO

    @classmethod
    def remover(cls,string:str) -> str:
        return re.sub(cls._regExp,' ',string,flags=cls._flags)
