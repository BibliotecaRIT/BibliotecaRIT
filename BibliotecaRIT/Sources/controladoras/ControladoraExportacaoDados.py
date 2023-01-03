from BibliotecaRIT.Sources.entidades.Projeto import Projeto
from BibliotecaRIT.Sources.estrategias.exportacao.VisaoRelevanciaTematicaPorStatus import VisaoRelevanciaTematicaPorStatus
from BibliotecaRIT.Sources.interfaces.VisaoStrategy import VisaoStrategy


class ControladoraExportacaoDados:
    _visao = VisaoRelevanciaTematicaPorStatus
 
    @classmethod
    def setVisaoStrategy(cls,visao:VisaoStrategy):
        cls._visao = visao
    
    @classmethod
    def gerarCSV(cls,projeto:Projeto, arg=""):
        cls._visao.exportarDadosGitHub(projeto,arg)