from BibliotecaRIT.Sources.interfaces.FiltroExtracaoStrategy import FiltroExtracaoStrategy


class FiltroExtracaoIssuesAbertas(FiltroExtracaoStrategy):

    @staticmethod
    def urlNumeroPaginas(usuario, repositorio) -> str:
        return 'https://api.github.com/repos/'+usuario+'/'+repositorio+'/issues?page{0}&per_page=100&state=open'

    @staticmethod
    def urlRequisicaoIssuesPorPagina(usuario, repositorio, numeroPagina) -> str:
         return 'https://api.github.com/repos/'+usuario+'/'+repositorio+'/issues?page='+str(numeroPagina)+'&per_page=100&state=open'
       