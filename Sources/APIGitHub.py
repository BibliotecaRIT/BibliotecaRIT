import requests

class APIGitHub:
    token = "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"
    headers = {'Authorization': 'token ' + token}

    @classmethod
    def numeroPaginasIssuesAbertas(cls, usuario, repositorio):
        url = 'https://api.github.com/repos/'+usuario+'/'+repositorio+'/issues?page{0}&per_page=100'
        response = requests.get(url, headers=cls.headers)

        if response.links.keys():
            return int(response.links['last']['url'].partition("&page=")[-1])

        else:
            return 1

    @classmethod
    def numeroPaginasIssuesFechadas(cls, usuario, repositorio):
        url = 'https://api.github.com/repos/'+usuario+'/'+repositorio+'/issues?page{0}&per_page=100&state=closed'
        response = requests.get(url, headers=cls.headers)

        if response.links.keys():
            return int(response.links['last']['url'].partition("&page=")[-1])

        else:
            return 1

    @classmethod
    def requisisaoIssuesAbertas(cls, usuario, repositorio, numeroPagina):
        url = 'https://api.github.com/repos/'+usuario+'/'+repositorio+'/issues?page='+str(numeroPagina)
        response = requests.get(url, headers=cls.headers).json()

        if response is not None:
            return response

    @classmethod
    def requisisaoIssuesFechadas(cls, usuario, repositorio, numeroPagina):
        url = 'https://api.github.com/repos/'+usuario+'/'+repositorio+'/issues?page='+str(numeroPagina)+'&state=closed'
        response = requests.get(url, headers=cls.headers).json()

        if response is not None:
            return response

    @classmethod
    def requisicaoComentarios(cls, usuario, repositorio, numeroIssue):
        url = 'https://api.github.com/repos/'+usuario+'/'+repositorio+'/issues/'+str(numeroIssue)+'/comments'
        response = requests.get(url, headers=cls.headers).json()

        if response is not None:
            return response