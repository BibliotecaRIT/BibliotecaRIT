import csv
from BibliotecaRIT.Sources.entidades.Projeto import Projeto
from BibliotecaRIT.Sources.entidades.Topico import Topico
from BibliotecaRIT.Sources.estrategias.exportacao.VisaoRelevanciaTematicaPorStatus import VisaoRelevanciaTematicaPorStatus
from BibliotecaRIT.Sources.estrategias.exportacao.VisaoStrategy import VisaoStrategy


class ControladoraExportacaoDados:
    _visao = VisaoRelevanciaTematicaPorStatus
 
    @classmethod
    def setVisaoStrategy(cls,visao:VisaoStrategy):
        cls._visao = visao
    
    @classmethod
    def gerarCSVs(cls, projeto:Projeto, visao, numPagina, arg):
        operacao = 'w' if numPagina == 1 else 'a'
        
        fileComentario = open(projeto.repositorio+"-comentarios-"+str(visao)+'.csv', operacao, encoding='utf-8')
        csvFileComentarios = csv.writer(fileComentario,escapechar="\\")
        
        fileIssues = open(projeto.repositorio+"-issues-"+str(visao)+'.csv', operacao, encoding='utf-8')
        csvFileIssues = csv.writer(fileIssues,escapechar="\\")

        # Gravando a Linha com o Título das Colunas
        if numPagina == 1:
            csvFileIssues.writerow(['NumeroIssue','IdIssue', 'TituloIssue', 'DescricaoIssue', 'CriacaoIssue','RepositorioIssue','LinkIssue'])
            csvFileComentarios.writerow(['IdIssue','NumeroComentario','Comentario', 'DataComentario', 
                                         'RelevanciaTematica', 'AutorComentario','Tags'])
        # Gravando as Linhas
        for topico in projeto.topicos:
            if len(topico.listaComentarios)!=0:
                cls.__exportarIssuesGitHub(topico,csvFileIssues,projeto.repositorio,)
                for comentario in topico.listaComentarios:
                    cls._visao.exportarComentariosGitHub(topico.id,comentario,csvFileComentarios,arg)
    
    def __exportarIssuesGitHub(topico:Topico,csvFile,repo:str):
        csvFile.writerow([topico.number,topico.id, topico.titulo, topico.descricao, topico.dataCriacao,repo,topico.link])