import csv
from BibliotecaRIT.Sources.entidades.Projeto import Projeto
from BibliotecaRIT.Sources.estrategias.exportacao.VisaoRelevanciaTematicaPorStatus import VisaoRelevanciaTematicaPorStatus
from BibliotecaRIT.Sources.estrategias.exportacao.VisaoStrategy import VisaoStrategy


class ControladoraExportacaoDados:
    _visao = VisaoRelevanciaTematicaPorStatus
 
    @classmethod
    def setVisaoStrategy(cls,visao:VisaoStrategy):
        cls._visao = visao
    
    @classmethod
    def gerarCSV(cls, projeto:Projeto, visao, numPagina, arg):
        operacao = 'w' if numPagina == 1 else 'a'
        file = open(projeto.repositorio+"-"+str(visao)+'.csv', operacao, newline='', encoding='utf-8')
        csvFile = csv.writer(file,escapechar="\\")

        # Gravando a Linha com o Título das Colunas
        if numPagina == 1:
            csvFile.writerow(['NumeroIssue', 'TituloIssue', 'DescricaoIssue', 'CriacaoIssue', 'NumeroComentario',
                        'Comentario', 'DataComentario', 'RelevanciaTematica', 'AutorComentario'])
        cls._visao.exportarDadosGitHub(projeto,csvFile,arg)