from abc import ABC, abstractmethod

class VisaoStrategy(ABC):

    @staticmethod
    @abstractmethod
    def exportarDadosGitHub(projeto,arg=""):
        pass