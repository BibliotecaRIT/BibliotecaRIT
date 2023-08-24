## Sobre a Biblioteca RIT

A biblioteca RIT (Relevance in Issue Tracking) analisa os comentários postados no ambiente de issue tracking do GitHub, por meio do cálculo da métrica de Relevância Temática dos mesmos. Essa métrica calcula quão relevantes os comentários são para uma discussão no contexto da issue (inclui pull requests por serem um tipo “especial” de issue). Os dados das issues com as respectivas relevâncias dos comentários são exportados em formato CSV, por meio de visões pré-selecionadas pela aplicação cliente. 

A biblioteca RIT faz parte dos esforços de modularização da ferramenta [Colminer](http://nupessc.caf.ufv.br/#/nupessc/projetos/colminer), sendo responsável, exclusivamente, pelo cálculo da principal métrica utilizada pela ferramenta, a relevância temática.

## Pré-requisitos
Para utilizar a biblioteca, basta ter instalado na sua máquina:
* [Python >= 3.10](https://www.python.org/downloads/)
* [PIP >= 22.3](https://www.makeuseof.com/tag/install-pip-for-python/)

## Instalação
Para instalar a biblioteca execute o comando:

No linux:

``` 
pip3 install Biblioteca-RIT
```

No Windows:
``` 
pip install Biblioteca-RIT
```
## Uso
1) Para que a biblioteca possa fazer as requisições no GitHub é necessário criar um [_personal access token_](https://docs.github.com/pt/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
    - Caso a biblioteca seja utilizada para calcular a relevância temática de um grande volume de dados, é recomendado fornecer mais de um token.

2) Importe a biblioteca RIT no seu arquivo fonte:
``` 
from BibliotecaRIT.BibliotecaRITFachada import  BibliotecaRITFachada
```
3) Instancie a biblioteca fornecendo os seus tokens, exemplo:
``` 
rit = BibliotecaRITFachada(tokens=[“token1”,”token2”,”token3”])
```
## Método calcularRelevanciaTematicaGitHub
A biblioteca dispõe de um único método a ser usado:
```
def calcularRelevanciaTematicaGitHub(self, usuario, repositorio, visao, arg, pagInicial)
```
Abaixo são descritas as informações necessárias para utilizar este método.
 No campo _usuario_, insira o  nome do dono do repositório a ser analisado.
 No campo _repositorio_, insira o nome do repositório a ser  analisado.
 No campo _visao_, selecione  o tipo de filtro que será aplicado às _ issues _ do repositórios especificados, sendo:  
* 1 para filtrar por comentários de _issues_ abertas
* 2 para filtrar por comentários de _issues_ fechadas
* 3 para filtrar por comentários de _issues_ abertas e fechadas
Caso não seja especificada nenhuma visão, esta será utilizada.
* 4 para filtrar comentários por  autor, tanto para issues abertas quanto  fechadas
* 5 para filtrar comentários por  data, para  issues abertas e fechadas
No campo _arg_, deve ser fornecido o nome do autor (usuário correspondente), no caso de ser  selecionado o filtro 4 OU a data, caso o filtro 5 tenha sido escolhido. Caso contrário, não é necessário utilizá-lo.
* O campo _pagInicial_ deve ser utilizado quando ocorrer algum erro durante a extração dos dados, como por exemplo, não forem extraídos os dados de todas as _issues_ do repositório por não possuir tokens suficientes ou erro de conexão com a internet. Assim, é possível reaproveitar os dados já extraídos e começar novamente o cálculo de relevância temática a partir da página de _issues_ que gerou erro. Por padrão, este campo possui valor 1, indicando que o cálculo de relevância será realizado a partir da primeira página.

Ao final da execução do método calcularRelevanciaTematicaGitHub(...), é gerado um arquivo CSV que contém os seguintes dados acerca das _issues_ e seus comentários: ID da _issue_, título da _issue_, descrição da _issue_, data de criação da issue, ID do comentário, comentário, data do comentário, Relevância Temática dos comentários e nome do autor do comentário.

## Exemplo de uso
No exemplo a seguir, ilustra-se como utilizar a biblioteca RIT para calcular a relevância temática dos comentários do seguinte repositório: [https://github.com/mockturtl/dotenv](https://github.com/mockturtl/dotenv).

### Instância da biblioteca

```
1 from BibliotecaRIT.BibliotecaRITFachada import  BibliotecaRITFachada
2 # Instância da biblioteca
3 rit = BibliotecaRITFachada(tokens=[“ghp…”])
````
- Utilizando o filtro 1

```
4 # Extrai e exporta em um arquivo CSV, dados sobre as issues abertas do repositório dotenv do usuário mockturtl
5 # com a relevância temática dos comentários
6 rit.calcularRelevanciaTematicaGitHub(usuario="mockturtl",repositorio="dotenv",visao=1)
```

- Utilizando o filtro 2
```
4 # Extrai e exporta em um arquivo CSV, dados sobre as issues fechadas do repositório dotenv do usuário mockturtl
5 # com a relevância temática dos comentários
6 rit.calcularRelevanciaTematicaGitHub(usuario="mockturtl",repositorio="dotenv",visao=2)
``` 
- Utilizando o filtro 3
```
4 # Extrai e exporta em um arquivo CSV, dados sobre as issues abertas e fechadas do repositório dotenv do usuário mockturtl
5 # com a relevância temática dos comentários
6 rit.calcularRelevanciaTematicaGitHub(usuario="mockturtl",repositorio="dotenv",visao=3)
```  
- Utilizando o filtro 4
```
4 # Extrai e exporta em um arquivo CSV, dados sobre as issues abertas e fechadas do repositório dotenv do usuário mockturtl 
5 # com a relevância temática dos comentários que contêm somente comentários do autor smayas
6 rit.calcularRelevanciaTematicaGitHub(usuario="mockturtl",repositorio="dotenv",visao=4,arg="smayas")
```
- Utilizando o filtro 5
```
4 # Extrai e exporta em um arquivo CSV, dados sobre as issues abertas e fechadas do repositório dotenv do usuário mockturtl
5 # com a relevância temática dos comentários que contêm somente comentários na data 15/07/2021
6 rit.calcularRelevanciaTematicaGitHub(usuario="mockturtl",repositorio="dotenv",visao=5,arg="2021-07-15")
``` 
### Saída
Ao executar algum dos exemplos acima, são gerados dois arquivos CSVs com os nomes _dotenv-comentarios-x.csv_ e _dotenv-issues-x_, onde x é número da visão que foi escolhida. Estes arquivos contém, respectivamente, os dados acerca dos comentários e das _issues_ do repositório dotenv.