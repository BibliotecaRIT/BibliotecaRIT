from BibliotecaRIT.Sources.estrategias.extracao.FiltroExtracaoStrategy import FiltroExtracaoStrategy


class FiltroExtracaoIssuesFechadas(FiltroExtracaoStrategy):

    @staticmethod
    def urlNumeroPaginas(usuario, repositorio) -> str:
        return 'https://api.github.com/repos/'+usuario+'/'+repositorio+'/issues?page{0}&per_page=100&state=closed'
        
    @staticmethod
    def urlRequisicaoIssuesPorPagina(usuario, repositorio, numeroPagina) -> str:
        return 'https://api.github.com/repos/'+usuario+'/'+repositorio+'/issues?page='+str(numeroPagina)+'&per_page=100&state=closed'
       