from BibliotecaRIT.Sources.estrategias.exportacao.FiltroExportacaoStrategy import VisaoStrategy

class VisaoRelevanciaTematicaPorData(VisaoStrategy):

    @staticmethod
    def exportarDadosGitHub(projeto, csvFile, arg):
        for i in range(len(projeto.topicos)):
            topico=projeto.topicos[i]
            if len(topico.listaComentarios)!=0:
                for comentario in topico.listaComentarios:
                # Filtrando por Data
                    if(arg in comentario.data):
                        csvFile.writerow([topico.number, topico.titulo, topico.descricao, topico.dataCriacao,
                                    comentario.id, comentario.mensagem, comentario.data, comentario.relevancia,
                                    comentario.loginAutor])
 