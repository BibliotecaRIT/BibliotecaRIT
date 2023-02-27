from abc import ABC, abstractmethod

class VisaoStrategy(ABC):
    @staticmethod
    @abstractmethod
    def exportarDadosGitHub(projeto,csvFile,arg):
        pass