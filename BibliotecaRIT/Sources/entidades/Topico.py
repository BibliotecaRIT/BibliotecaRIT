class Topico:
    def __init__(self,  id, loginAutor, dataCriacao, dataFechamento, url, titulo, descricao, status, number=0):
        self._id = id
        self.loginAutor = loginAutor
        self._dataCriacao = dataCriacao
        self.dataFechamento = dataFechamento
        self.url = url
        self._number = number
        self._titulo = titulo
        self._descricao = descricao
        self.status = status
        self._listaComentarios = []
        
    def inserirComentarios(self, listaComentarios):
        self._listaComentarios = listaComentarios
        
    @property
    def number(self):
        return self._number
    
    @property
    def id(self):
        return self._id
    
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