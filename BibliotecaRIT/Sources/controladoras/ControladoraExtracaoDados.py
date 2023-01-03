from BibliotecaRIT.Sources.Requisicao import Requisicao
from BibliotecaRIT.Sources.entidades.Comentario import Comentario
from BibliotecaRIT.Sources.entidades.Projeto import Projeto
from BibliotecaRIT.Sources.entidades.Topico import Topico
from BibliotecaRIT.Sources.estrategias.extracao.FiltroExtracaoIssuesAbertas import FiltroExtracaoIssuesAbertas
from BibliotecaRIT.Sources.interfaces.FiltroExtracaoStrategy import FiltroExtracaoStrategy


class ControladoraExtracaoDados:
    _requisicao = Requisicao
    _filtroExtracao = FiltroExtracaoIssuesAbertas

    @classmethod
    def setFiltroExtracaoStrategy(cls,filtroExtracaoStrategy:FiltroExtracaoStrategy):
        cls._filtroExtracao = filtroExtracaoStrategy

    @classmethod
    def _numeroPaginas(cls,usuario, repositorio):
        url = cls._filtroExtracao.urlNumeroPaginas(usuario,repositorio)
        response = cls._requisicao.request(url=url)
        if response.links.keys():
            return int(response.links['last']['url'].partition("&page=")[-1])
        else:
            return 1
    
    @classmethod
    def _requisicaoIssuesPorPagina(cls,usuario, repositorio, numeroPagina):
        url = cls._filtroExtracao.urlRequisicaoIssuesPorPagina(usuario,repositorio,numeroPagina)
        response = cls._requisicao.request(url=url).json()
        if response is not None:
            return response
    
    @classmethod
    def _requisicaoComentariosPorIssue(cls, usuario, repositorio, numeroIssue):
        url = 'https://api.github.com/repos/'+usuario+'/'+repositorio+'/issues/'+str(numeroIssue)+'/comments'
        response = cls._requisicao.request(url=url).json()
        if response is not None:
            return response
    
    @classmethod
    def requisicaoIssues(cls,usuario:str,repositorio:str):
        topicos= []
        numeroPaginas = cls._numeroPaginas(usuario, repositorio)
        for i in range(1, numeroPaginas+1):
            dadosIssues = cls._requisicaoIssuesPorPagina(usuario, repositorio, i)
            for j in range(len(dadosIssues)):
                # Inicializando uma Issue
                topico = Topico(dadosIssues[j]['id'], dadosIssues[j]['user']['login'], dadosIssues[j]['created_at'], dadosIssues[j]['closed_at'], dadosIssues[j]['url'], dadosIssues[j]['title'], dadosIssues[j]['body'], dadosIssues[j]['state'], dadosIssues[j]['author_association'], dadosIssues[j]['number'])

                # Requisitando os Comentários de cada Issue
                dadosComentarios = cls._requisicaoComentariosPorIssue(usuario, repositorio, dadosIssues[j]['number'])
                comentarios = []

                for k in range(len(dadosComentarios)):
                    # Inserindo os Dados dos Comentários da Issue
                    comentario = Comentario(dadosComentarios[k]['id'], dadosIssues[j]['id'], dadosComentarios[k]['user']['login'], dadosComentarios[k]['body'], dadosComentarios[k]['created_at'])
                    comentarios.append(comentario)

                # Inserindo Dados da Issue
                # Instanciando os Comentários na Issue, e Salvando a Issue na Lista
                topico.inserirComentarios(comentarios)
                topicos.append(topico)
            print(f"Extração dos dados - Página número {i}/{numeroPaginas} finalizada")
        projeto = Projeto(usuario, repositorio, topicos)
        return projeto
    
