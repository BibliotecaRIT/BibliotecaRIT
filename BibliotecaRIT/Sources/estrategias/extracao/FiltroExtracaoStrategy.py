from abc import ABC, abstractmethod

class FiltroExtracaoStrategy(ABC):
    
    @staticmethod
    @abstractmethod
    def urlNumeroPaginas(usuario,repositorio) -> str:
        pass
    
    @staticmethod
    @abstractmethod
    def urlRequisicaoIssuesPorPagina(usuario, repositorio, numeroPagina) -> str:
        pass
