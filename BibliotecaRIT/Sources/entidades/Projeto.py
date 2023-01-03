class Projeto:
    def __init__(self, usuario, repositorio, topicos):
        self._usuario = usuario
        self._repositorio = repositorio
        self._topicos = topicos

    @property
    def usuario(self):
        return self._usuario

    @property
    def repositorio(self):
        return self._repositorio

    @property
    def topicos(self):
        return self._topicos