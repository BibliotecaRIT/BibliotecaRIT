class Comentario:
    def __init__(self, id, idTopico, loginAutor, mensagem, data, reputacao=0):
        self._id = id
        self.idTopico = idTopico
        self._loginAutor = loginAutor
        self._mensagem = mensagem
        self._data = data
        self._relevancia = 0
        self._reputacao = reputacao
        
    def inserirRelevanciaTematica(self, relevancia):
        self._relevancia = relevancia
        
    @property
    def relevancia(self):
        return self._relevancia
    
    @property
    def mensagem(self):
        return self._mensagem
    
    @property
    def data(self):
        return self._data
    
    @property
    def loginAutor(self):
        return self._loginAutor
    
    @property
    def id(self):
        return self._id
    
    @property
    def reputacao(self):
        return self._reputacao