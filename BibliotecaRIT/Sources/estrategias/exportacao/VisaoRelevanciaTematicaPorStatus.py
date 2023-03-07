from BibliotecaRIT.Sources.estrategias.exportacao.VisaoStrategy import VisaoStrategy

class VisaoRelevanciaTematicaPorStatus(VisaoStrategy):
   
   @staticmethod
   def exportarDadosGitHub(projeto, csvFile, arg):
    # Gravando as Linhas
    for i in range(len(projeto.topicos)):
        topico=projeto.topicos[i]
        if len(topico.listaComentarios)!=0:
            for comentario in topico.listaComentarios:                            
                csvFile.writerow([topico.number, topico.titulo, topico.descricao, topico.dataCriacao,
                                comentario.id, comentario.mensagem, comentario.data, comentario.relevancia,
                                comentario.loginAutor])
