from copy import deepcopy
from BibliotecaRIT.Sources.Requisicao import Requisicao
from BibliotecaRIT.Sources.controladoras.ControladoraCalculoRelevancia import ControladoraCalculoRelevancia
from BibliotecaRIT.Sources.controladoras.ControladoraExportacaoDados import ControladoraExportacaoDados
from BibliotecaRIT.Sources.controladoras.ControladoraExtracaoDados import ControladoraExtracaoDados
from BibliotecaRIT.Sources.controladoras.ControladoraPreProcessamento import ControladoraPreProcessamento
from BibliotecaRIT.Sources.entidades.Projeto import Projeto
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
            
            print(f'-- Pré-processando os dados da página {i}/{qtdPaginas} do repositório {repositorio} --')
            projetoPreProcessado = cls.__preProcessarProjeto(projeto)

            print(f'-- Calculando a Relevância Temática dos Comentários da página {i}/{qtdPaginas} do repositório {repositorio} --')
            cls.__calcularRelevanciaTematicaComentariosGitHub(projeto,projetoPreProcessado)
     
            print(f'-- Exportando dados da página {i}/{qtdPaginas} do repositório {repositorio} --')
            cls.__gerarCSVGitHub(projeto, visao, i, arg)
            
            print('\033[92m' + f'Página {i}/{qtdPaginas} do repositório {repositorio} finalizada' + '\033[0m')
            print()

    @staticmethod
    def __preProcessarProjeto(projeto:Projeto)-> Projeto:
        copiaProjeto = deepcopy(projeto)
        preProcessamento = ControladoraPreProcessamento
        for i in range(len(projeto.topicos)):
            topico = copiaProjeto.topicos[i]
            descricaoPreProcessada = preProcessamento.processar(topico.descricao)[0]
            topico.setDescricao(descricaoPreProcessada)
            for j in range(len(topico.listaComentarios)):
                comentario = topico.listaComentarios[j]
                comentarioPreProcessado, tags = preProcessamento.processar(comentario.mensagem)
                projeto.topicos[i].listaComentarios[j].setTags(tags)
                comentario.setMensagem(comentarioPreProcessado)
        return copiaProjeto
    
    @staticmethod
    def __calcularRelevanciaTematicaComentariosGitHub(projeto:Projeto,projetoPreProcessado:Projeto):
        comentariosAnteriores = ''
        for i in range (len(projetoPreProcessado.topicos)):
            topico = projetoPreProcessado.topicos[i]
            for j in range((len(topico.listaComentarios))):
                comentario = topico.listaComentarios[j] 
                relevancia = ControladoraCalculoRelevancia.relevanciaTematica(comentario.mensagem, comentariosAnteriores, (str(topico.titulo) + str(topico.descricao)))
                comentariosAnteriores += comentario.mensagem
                projeto.topicos[i].listaComentarios[j].inserirRelevanciaTematica(relevancia)
    
    @staticmethod
    def __gerarCSVGitHub(projeto:Projeto, visao,numPagina, arg ):
        if(visao == 4):
            ControladoraExportacaoDados.setVisaoStrategy(visao=VisaoRelevanciaTematicaPorAutor)
        elif(visao == 5):
            ControladoraExportacaoDados.setVisaoStrategy(visao=VisaoRelevanciaTematicaPorData)
        return ControladoraExportacaoDados.gerarCSVs(projeto,visao,numPagina,arg)
    
    
