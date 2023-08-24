from BibliotecaRIT.Sources.entidades.Tags import Tags
from BibliotecaRIT.Sources.estrategias.preProcessamento.PreProcessamentoCaminho import PreProcessamentoCaminho
from BibliotecaRIT.Sources.estrategias.preProcessamento.codigo.PreProcessamentoCodigoInlineHTML import PreProcessamentoCodigoInlineHTML
from BibliotecaRIT.Sources.estrategias.preProcessamento.codigo.PreProcessamentoCodigoInlineMardown import PreProcessamentoCodigoInlineMarkdown
from BibliotecaRIT.Sources.estrategias.preProcessamento.codigo.PreProcessamentoTrechoCodigoHTML import PreProcessamentoTrechoCodigoHTML
from BibliotecaRIT.Sources.estrategias.preProcessamento.PreProcessamentoDetailsHTML import  PreProcessamentoDetailsHTML
from BibliotecaRIT.Sources.estrategias.preProcessamento.codigo.PreProcessamentoTrechoCodigoMarkdown import  PreProcessamentoTrechoCodigoMarkdown
from BibliotecaRIT.Sources.estrategias.preProcessamento.PreProcessamentoEmail import PreProcessamentoEmail
from BibliotecaRIT.Sources.estrategias.preProcessamento.PreProcessamentoEmoji import PreProcessamentoEmoji
from BibliotecaRIT.Sources.estrategias.preProcessamento.imagem.PreProcessamentoImagemHTML import PreProcessamentoImagemHTML
from BibliotecaRIT.Sources.estrategias.preProcessamento.PreProcessamentoNomeUsuario import PreProcessamentoNomeUsuario
from BibliotecaRIT.Sources.estrategias.preProcessamento.imagem.PreProcessamentoImagemMarkdown import  PreProcessamentoImagemMarkdown
from BibliotecaRIT.Sources.estrategias.preProcessamento.url.PreProcessamentoURL import PreProcessamentoURL
from BibliotecaRIT.Sources.estrategias.preProcessamento.url.PreProcessamentoURLHTML import PreProcessamentoURLHTML
from BibliotecaRIT.Sources.estrategias.preProcessamento.url.PreProcessamentoURLMarkdown import PreProcessamentoURLMarkdown

class ControladoraPreProcessamento:
    # **CUIDADO**: Alterar a sequência pode alterar o resultado do pré-processamento
    _estrategias = [
        PreProcessamentoEmail,
        PreProcessamentoEmoji,
        PreProcessamentoNomeUsuario,
        PreProcessamentoImagemHTML,
        PreProcessamentoImagemMarkdown,
        PreProcessamentoDetailsHTML,
        PreProcessamentoTrechoCodigoHTML,
        PreProcessamentoCodigoInlineHTML,
        PreProcessamentoTrechoCodigoMarkdown,
        PreProcessamentoCodigoInlineMarkdown,
        PreProcessamentoURLMarkdown,
        PreProcessamentoURLHTML,
        PreProcessamentoURL,
        PreProcessamentoCaminho, 
    ]

    @classmethod
    def processar(cls, mensagem: str):
        tags = Tags()
        for estrategia in cls._estrategias:
            if estrategia.contem(mensagem):
                tag = estrategia.getTag()
                tags.addTag(tag)
                mensagem = estrategia.remover(
                    mensagem)
        return mensagem, tags

