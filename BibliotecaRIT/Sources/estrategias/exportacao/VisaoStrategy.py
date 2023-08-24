from abc import ABC, abstractmethod

from BibliotecaRIT.Sources.entidades.Comentario import Comentario

class VisaoStrategy(ABC):

    @staticmethod
    @abstractmethod
    def exportarComentariosGitHub(idTopico:int,comentario:Comentario,csvFile,arg:str):
        pass