from stackapi import StackAPI
import html
import re

class APIStackOverflow:
    @classmethod
    def requisicaoPergunta(self, id, site):
        pergunta = site.fetch('questions/{}'.format(id), filter='withbody')

        try:
            pergunta['items'][0]['title'] = html.unescape(pergunta['items'][0]['title'])
            pergunta['items'][0]['body'] = APIStackOverflow.retirarTagHTML(pergunta['items'][0]['body'])

        except IndexError:
            pergunta['items']['title'] = html.unescape(pergunta['items']['title'])
            pergunta['items']['body'] = APIStackOverflow.retirarTagHTML(pergunta['items']['body'])

        return pergunta

    @classmethod
    def requisicaoRespostas(self, id, site):
        respostas = site.fetch('questions/{}/answers'.format(id), filter='withbody')
        
        for i in range(len(respostas['items'])):
            respostas['items'][i]['body'] = APIStackOverflow.retirarTagHTML(respostas['items'][i]['body'])
        
        return respostas

    @classmethod
    def requisicaoComentariosRespostas(self):
        pass

    @classmethod
    def retirarTagHTML(self, texto):
        # Retirar \n
        texto = texto.replace("\n", "")

        # Retirar trechos de Código
        texto = re.sub("<code>(.*?)</code>", "", texto)

        # Retirar demais tag HTML
        texto = re.sub('<[^>]+?>', ' ', texto)

        return texto