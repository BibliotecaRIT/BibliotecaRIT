from BibliotecaRIT.Sources.entidades.Comentario import Comentario
from BibliotecaRIT.Sources.entidades.Topico import Topico
from BibliotecaRIT.Sources.estrategias.exportacao.VisaoStrategy import VisaoStrategy


class VisaoRelevanciaTematicaPorData(VisaoStrategy):

    @staticmethod
    def exportarComentariosGitHub(idTopico: int, comentario: Comentario, csvFile, arg: str):
        if(arg in comentario.data):
            csvFile.writerow([idTopico,comentario.id, comentario.mensagem, comentario.data,
                               comentario.relevancia,comentario.loginAutor,comentario.tagsToString()])
