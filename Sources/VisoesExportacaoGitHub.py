# Import das Classes de Inserção dos Dados Extraídos
from Sources.Projeto import Projeto
from Sources.Topico import Topico
from Sources.Comentario import Comentario

# Import da Biblioteca de Extração de Dados em CSV
import csv

class VisaoExportacaoGitHub:
    @classmethod
    def exportacaoIssuesAbertasFechadas(cls, projeto):
        # Criando o Arquivo
        f = open((projeto.repositorio+'.csv'), 'w', newline='', encoding='utf-8')

        # Criando o Objeto de Gravação
        w = csv.writer(f)
        
        # Gravando a Linha com o Título das Colunas
        w.writerow(['NumeroIssue', 'TituloIssue', 'DescricaoIssue', 'CriacaoIssue', 'NumeroComentario',
                    'Comentario', 'DataComentario', 'RelevanciaTematica', 'AutorComentario'])

        # Gravando as Linhas
        for topico in projeto.topicos:
            for comentario in topico.listaComentarios:
                w.writerow([topico.number, topico.titulo, topico.descricao, topico.dataCriacao,
                            comentario.id, comentario.mensagem, comentario.data, comentario.relevancia,
                            comentario.loginAutor])
    
    @classmethod
    def exportacaoIssuesAutor(cls, projeto, autor):
        # Criando o Arquivo
        f = open((projeto.repositorio+'.csv'), 'w', newline='', encoding='utf-8')

        # Criando o Objeto de Gravação
        w = csv.writer(f)
        
        # Gravando a Linha com o Título das Colunas
        w.writerow(['NumeroIssue', 'TituloIssue', 'DescricaoIssue', 'CriacaoIssue', 'NumeroComentario',
                    'Comentario', 'DataComentario', 'RelevanciaTematica', 'AutorComentario'])

        # Gravando as Linhas
        for topico in projeto.topicos:
            for comentario in topico.listaComentarios:
                if(comentario.loginAutor == autor):
                    w.writerow([topico.number, topico.titulo, topico.descricao, topico.dataCriacao,
                                comentario.id, comentario.mensagem, comentario.data, comentario.relevancia,
                                comentario.loginAutor])
    
    @classmethod
    def exportacaoIssuesData(cls, projeto, data):
        pass