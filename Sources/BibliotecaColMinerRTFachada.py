# Importe das APIs de Extração de Dados
from Sources.APIGitHub import APIGitHub
from Sources.APIStackOverflow import APIStackOverflow
from stackapi import StackAPI

# Import das Classes de Inserção dos Dados Extraídos
from Sources.Projeto import Projeto
from Sources.Topico import Topico
from Sources.Comentario import Comentario

# Importa da Classe de Cálculo de Relevância Temática e Exportação em CSV
from Sources.CalculoRelevancia import CalculoRelevancia
import csv

class BibliotecaColMinerRTFachada:
    @classmethod
    def processarDadosGitHub(cls, usuario, repositorio, tipoIssue):
        # Requisitando os Dados das Issues do Projeto
        # A Requisição é feita de Acordo com o Número de Páginas
        if(tipoIssue == 1):
            numeroPaginas = APIGitHub.numeroPaginasIssuesAbertas(usuario, repositorio)
        else:
            numeroPaginas = APIGitHub.numeroPaginasIssuesFechadas(usuario, repositorio)
        
        topicos = []

        for i in range(1, numeroPaginas+1):
            if(tipoIssue == 1):
                dadosIssues = APIGitHub.requisisaoIssuesAbertas(usuario, repositorio, i)
            else:
                dadosIssues = APIGitHub.requisisaoIssuesFechadas(usuario, repositorio, i)
            
            for j in range(len(dadosIssues)):
                # Inicializando uma Issue
                topico = Topico(dadosIssues[j]['id'], dadosIssues[j]['user']['login'], dadosIssues[j]['created_at'], dadosIssues[j]['closed_at'], dadosIssues[j]['url'], dadosIssues[j]['title'], dadosIssues[j]['body'], dadosIssues[j]['state'], dadosIssues[j]['author_association'], dadosIssues[j]['number'])

                # Requisitando os Comentários de cada Issue
                dadosComentarios = APIGitHub.requisicaoComentarios(usuario, repositorio, dadosIssues[j]['number'])
                comentarios = []

                for k in range(len(dadosComentarios)):
                    # Inserindo os Dados dos Comentários da Issue
                    comentario = Comentario(dadosComentarios[k]['id'], dadosIssues[j]['id'], dadosComentarios[k]['user']['login'], dadosComentarios[k]['body'], dadosComentarios[k]['created_at'])
                    comentarios.append(comentario)

                # Inserindo Dados da Issue
                # Instanciando os Comentários na Issue, e Salvando a Issue na Lista
                topico.inserirComentarios(comentarios)
                topicos.append(topico)
                    

        # Inserindo os Dados da Classe Projeto
        projeto = Projeto(usuario, repositorio, topicos)
        return projeto

    @classmethod
    def processarDadosStackOverflow(cls, id, idioma):
        site = " "

        if (idioma == 'pt'):
            site = StackAPI('pt.stackoverflow', key='nuRIkglSnoAWqy*1ncLWcA((')

        elif (idioma == 'en'):
            site = StackAPI('stackoverflow', key='nuRIkglSnoAWqy*1ncLWcA((')

        pergunta = APIStackOverflow.requisicaoPergunta(id, site)
        status = False
        
        # Inserindo Informações do Topico
        topico = Topico(pergunta['items'][0]['question_id'], pergunta['items'][0]['owner']['display_name'], pergunta['items'][0]['creation_date'], pergunta['items'][0]['last_activity_date'], pergunta['items'][0]['link'], pergunta['items'][0]['title'], pergunta['items'][0]['body'], status)
        
        # Gerando as Informações dos Comentários, e Inserindo os Mesmos
        respostas = APIStackOverflow.requisicaoRespostas(id, site)
        comentarios = []
        
        for i in range(len(respostas['items'])):
            try:
                comentario = Comentario(respostas['items'][i]['answer_id'], respostas['items'][i]['question_id'], respostas['items'][i]['owner']['display_name'], respostas['items'][i]['body'], respostas['items'][i]['creation_date'], respostas['items'][i]['owner']['reputation'])
            except KeyError:
                comentario = Comentario(respostas['items'][i]['answer_id'], respostas['items'][i]['question_id'], respostas['items'][i]['owner']['display_name'], respostas['items'][i]['body'], respostas['items'][i]['creation_date'])
            
            comentarios.append(comentario)
        
        topico.inserirComentarios(comentarios)
        return topico

    @classmethod
    def calcularRelevanciaTematicaGitHub(cls, projeto):
        comentariosAnteriores = ''
        
        for topico in projeto.topicos:
            for comentario in topico.listaComentarios:
                relevancia = CalculoRelevancia.relevanciaTematica(comentario.mensagem, comentariosAnteriores, (str(topico.titulo) + str(topico.descricao)))
                comentariosAnteriores += comentario.mensagem
                comentario.inserirRelevanciaTematica(relevancia)
    
    @classmethod
    def calcularRelevanciaTematicaStackOverflow(cls, topico):
        comentariosAnteriores = ''
        
        for comentario in topico.listaComentarios:
            relevancia = CalculoRelevancia.relevanciaTematica(comentario.mensagem, comentariosAnteriores, (topico.titulo + topico.descricao))
            comentariosAnteriores += comentario.mensagem
            comentario.inserirRelevanciaTematica(relevancia)

    @classmethod
    def gerarCSVGitHub(cls, projeto):
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
    def gerarCSVStackOverflow(cls, topico):
        # Criando o Arquivo
        f = open(('topicoStack'+str(topico.id)+'.csv'), 'w', newline='', encoding='utf-8')

        # Criando o Objeto de Gravação
        w = csv.writer(f)
        
        # Gravando a Linha com o Título das Colunas
        w.writerow(['NumeroTopico', 'TituloTopico', 'DescricaoTopico', 'CriacaoTopico', 'NumeroComentario',
                    'Comentario', 'DataComentario', 'RelevanciaTematica', 'AutorComentario', 'Reputacao'])

        # Gravando as Linhas
        for comentario in topico.listaComentarios:
            w.writerow([topico.id, topico.titulo, topico.descricao, topico.dataCriacao,
                        comentario.id, comentario.mensagem, comentario.data, comentario.relevancia,
                        comentario.loginAutor, comentario.reputacao])