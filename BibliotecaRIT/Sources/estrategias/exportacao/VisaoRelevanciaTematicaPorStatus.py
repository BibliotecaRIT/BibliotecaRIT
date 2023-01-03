import csv
from BibliotecaRIT.Sources.interfaces.VisaoStrategy import VisaoStrategy


class VisaoRelevanciaTematicaPorStatus(VisaoStrategy):
   
   @staticmethod
   def exportarDadosGitHub(projeto, arg=""):
        particao = 0
        contador = 0
        contadorTopico = 1
        # Criando o Arquivo
        f = open(projeto.repositorio+"-"+str(particao)+'.csv', 'w', newline='', encoding='utf-8')

        # Criando o Objeto de Gravação
        w = csv.writer(f)
        
        # Gravando a Linha com o Título das Colunas
        w.writerow(['NumeroIssue', 'TituloIssue', 'DescricaoIssue', 'CriacaoIssue', 'NumeroComentario',
                    'Comentario', 'DataComentario', 'RelevanciaTematica', 'AutorComentario'])

        # Gravando as Linhas
        for topico in projeto.topicos:
            if len(topico.listaComentarios)!=0:
                if contador%20000 == 0 and contador!=0 :
                    particao += 1
                    f = open(projeto.repositorio+"-"+str(particao)+'.csv', 'w', newline='', encoding='utf-8')
                    w = csv.writer(f)    
                    w.writerow(['NumeroIssue', 'TituloIssue', 'DescricaoIssue', 'CriacaoIssue', 'NumeroComentario',
                                    'Comentario', 'DataComentario', 'RelevanciaTematica', 'AutorComentario'])
                    contador = 0
                   

                for comentario in topico.listaComentarios:
                        w.writerow([topico.number, topico.titulo, topico.descricao, topico.dataCriacao,
                                    comentario.id, comentario.mensagem, comentario.data, comentario.relevancia,
                                    comentario.loginAutor])
                contador+=1
            print(f"Exportação dos dados - Topico {contadorTopico}/{len(projeto.topicos)} finalizado.")
            contadorTopico+=1