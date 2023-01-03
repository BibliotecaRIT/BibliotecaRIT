from BibliotecaRIT.Sources.interfaces.FiltroExtracaoStrategy import FiltroExtracaoStrategy


class FiltroExtracaoIssuesAbertasFechadas(FiltroExtracaoStrategy):

    @staticmethod
    def urlNumeroPaginas( usuario, repositorio) -> str:
        return 'https://api.github.com/repos/'+usuario+'/'+repositorio+'/issues?page{0}&per_page=100&state=all'
       
    @staticmethod
    def urlRequisicaoIssuesPorPagina( usuario, repositorio, numeroPagina):
        return 'https://api.github.com/repos/'+usuario+'/'+repositorio+'/issues?page='+str(numeroPagina)+'&per_page=100&state=all'
        