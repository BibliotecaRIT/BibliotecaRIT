class Topico:
    def __init__(self, dataCriacao, titulo, descricao, number=0):
        self._dataCriacao = dataCriacao
        self._number = number
        self._titulo = titulo
        self._descricao = descricao
        self._listaComentarios = []
        
    def inserirComentarios(self, listaComentarios):
        self._listaComentarios = listaComentarios
        
    @property
    def number(self):
        return self._number
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def descricao(self):
        return self._descricao
    
    @property
    def dataCriacao(self):
        return self._dataCriacao
    
    @property
    def listaComentarios(self):
        return self._listaComentarios