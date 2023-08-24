from BibliotecaRIT.Sources.entidades.Comentario import Comentario
from BibliotecaRIT.Sources.estrategias.exportacao.VisaoStrategy import VisaoStrategy

class VisaoRelevanciaTematicaPorStatus(VisaoStrategy):
   
   @staticmethod
   def exportarComentariosGitHub(idTopico: int, comentario: Comentario, csvFile, arg: str):
         csvFile.writerow([idTopico,comentario.id, comentario.mensagem, comentario.data,
                           comentario.relevancia, comentario.loginAutor,comentario.tagsToString()])
