from BibliotecaRIT.Sources.estrategias.exportacao.VisaoStrategy import VisaoStrategy

class VisaoRelevanciaTematicaPorData(VisaoStrategy):

    @staticmethod
    def exportarDadosGitHub(projeto, csvFile, arg):
        for topico in projeto.topicos:
            if len(topico.listaComentarios)!=0:
                for comentario in topico.listaComentarios:
                # Filtrando por Data
                    if(arg in comentario.data):
                        csvFile.writerow([topico.number, topico.titulo, topico.descricao, topico.dataCriacao,
                                    comentario.id, comentario.mensagem, comentario.data, comentario.relevancia,
                                    comentario.loginAutor])
 