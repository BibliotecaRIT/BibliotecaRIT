from BibliotecaRIT.Sources.Requisicao import Requisicao
from BibliotecaRIT.Sources.controladoras.ControladoraCalculoRelevancia import ControladoraCalculoRelevancia
from BibliotecaRIT.Sources.controladoras.ControladoraExportacaoDados import ControladoraExportacaoDados
from BibliotecaRIT.Sources.controladoras.ControladoraExtracaoDados import ControladoraExtracaoDados
from BibliotecaRIT.Sources.estrategias.exportacao.VisaoRelevanciaTematicaPorData import VisaoRelevanciaTematicaPorData
from BibliotecaRIT.Sources.estrategias.exportacao.VisaoRelevanciaTematicaPorAutor import VisaoRelevanciaTematicaPorAutor


class BibliotecaRITFachada:
    def __init__(self, tokens=[]):
        Requisicao.init_tokens(tokens=tokens)

    @classmethod
    def calcularRelevanciaTematicaGitHub(cls,usuario, repositorio, visao=3, arg="", pagInicial=1):
        tipoIssue = visao if visao < 4 else 3
        ControladoraExtracaoDados.setFiltroExtracaoPorTipoIssue(tipoIssue)
        qtdPaginas = ControladoraExtracaoDados.numeroPaginas(usuario,repositorio)
        for i in range(pagInicial,qtdPaginas+1):
            print(f'-- Extraindo os dados da página {i}/{qtdPaginas} do repositório {repositorio} --')
            projeto = ControladoraExtracaoDados.requisicaoIssuesPorPagina(usuario,repositorio,i)
            print()
           
            print(f'-- Calculando a Relevância Temática dos Comentários da página {i}/{qtdPaginas} do repositório {repositorio} --')
            cls.__calcularRelevanciaTematicaComentariosGitHub(projeto)
            print()
            
            print(f'-- Gerando o arquivo .csv com da página {i}/{qtdPaginas} do repositório {repositorio} --')
            number = cls.__gerarCSVGitHub(projeto, visao, i, arg)
            
            if number != -1:
                print(f"Número da última issue exportada da página {i} - {number}.")
            else:
                print(f"issues dessa página não possuem comentários.")

            print()

    @staticmethod
    def __calcularRelevanciaTematicaComentariosGitHub(projeto):
        comentariosAnteriores = ''
        for topico in projeto.topicos:
            for comentario in topico.listaComentarios:
                relevancia = ControladoraCalculoRelevancia.relevanciaTematica(comentario.mensagem, comentariosAnteriores, (str(topico.titulo) + str(topico.descricao)))
                comentariosAnteriores += comentario.mensagem
                comentario.inserirRelevanciaTematica(relevancia)
    
    @staticmethod
    def __gerarCSVGitHub(projeto, visao,numPagina, arg ):
        if(visao == 4):
            ControladoraExportacaoDados.setVisaoStrategy(visao=VisaoRelevanciaTematicaPorAutor)
        elif(visao == 5):
            ControladoraExportacaoDados.setVisaoStrategy(visao=VisaoRelevanciaTematicaPorData)
        return ControladoraExportacaoDados.gerarCSV(projeto,visao,numPagina,arg)
    
    
