import inspect
import os
import requests
import numpy as np


class Requisicao:
    _tokens = []

    @classmethod
    def init_tokens(cls, tokens: list):
        cls._tokens = tokens 

    @classmethod
    def request(cls, url):
        tokens = cls._tokens.copy()
        for i in range(len(tokens)):
            try:
                headers = {'Authorization': 'token ' + tokens[i]}
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    return response
                else:
                    cls._tokens.pop(i)
            except Exception as e:
                cls._tokens.pop(i)
