class Topico:
    def __init__(self, dataCriacao, titulo, descricao, number,link,id=0):
        self._dataCriacao = dataCriacao
        self._id = id
        self._number = number
        self._titulo = titulo
        self._link = link
        self._descricao = descricao if descricao is not None else " "
        self._listaComentarios = []
        
    def inserirComentarios(self, listaComentarios):
        self._listaComentarios = listaComentarios
        
    def setDescricao(self, descricao:str):
        self._descricao = descricao
        
    @property
    def id(self):
        return self._id
    @property
    def link(self):
        return self._link
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