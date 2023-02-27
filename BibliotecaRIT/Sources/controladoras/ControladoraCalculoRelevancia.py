from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

class ControladoraCalculoRelevancia:
    @classmethod
    def similaridade(cls, texto1, texto2):
        # Gerando o Vetor como um Ngrama
        vect = CountVectorizer(analyzer = 'word', ngram_range= (1, 2))
        
        # Gerando o Vocabulário
        vocabulario = vect.fit([texto1, texto2])
        
        # Gerando Matriz com Valores de Palavras Similares nos textos
        matrizSimilaridade = vect.fit_transform([texto1, texto2])
        matrizSimilaridade = matrizSimilaridade.toarray()
        
        # Fazendo a Intersecção entre ambos, e gerando a soma do mesmo
        # e da matriz de similaridade
        interseccao = np.amin(matrizSimilaridade, axis = 0)
        soma = np.sum(interseccao)
        somaMatriz = np.sum(matrizSimilaridade[0])
        
        return soma/somaMatriz
    
    @classmethod
    def relevanciaTematica(cls, comentario, comentariosAnteriores, issue):
        # Calculando a Similaridade do Comentário com a Issue
        SCI = cls.similaridade(issue, comentario)
        
        # Calculando a Similaridade do Comentário com a discussão
        SCD = cls.similaridade((issue + comentariosAnteriores), comentario)
        
        return ((SCI+SCD)/2)