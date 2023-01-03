# **ColMiner**

O projeto ColMiner tem como objetivo analisar dados de ambientes de issue tracking com o intuito de apoiar o gerenciamento das comunicações em projetos de software. Para isso, a principal métrica utilizada nas análises é a relevância temática dos comentários postados nas issues associada a outras medidas quantitativas que possam revelar possíveis falhas de comunicação.

<br>

## **Sobre a biblioteca RIT**

A biblioteca RIT (Relevance in Issue Tracking) faz parte dos refinamentos e extensões da ferramenta ColMiner, em que suas macro-funcionalidades serão modularizadas e estendidas. Essa biblioteca analisa os comentários postados no ambiente de issue tracking do GitHub, por meio do cálculo da Relevância Temática dos mesmos, ou seja, calcula-se quão relevantes os comentários são para uma discussão. Através da biblioteca RIT, é possível:
<br>

* Calcular o quão relevante é cada comentário para o tema da discussão de uma _issue_ no GitHub;
* Exportar os dados relacionados as _issues_ junto com a relevência temática dos comentários através do formato CSV.


<br>

## **Pré-requisitos**
Para utilizar a biblioteca basta ter instalado na sua máquina:
* [Python](https://www.python.org/downloads/)   
* [Git](https://github.com/git-guides/install-git)
* [PIP](https://www.makeuseof.com/tag/install-pip-for-python/)


## **Instalação e uso**
Siga as etapas abaixo para utilizar a biblioteca RIT:

1) Na pasta raíz do seu projeto clone este repositório com o comando: 
``` 
git clone https://github.com/BibliotecaRIT/BibliotecaRIT.git
```  
2) Após a etapa acima execute o seguinte comando para instalar as dependências da biblioteca:
``` 
pip install -r BibliotecaRIT/requirements.txt
```
3) Para realizar as requisições é necessário inserir um [_personal access token_](https://docs.github.com/pt/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). Para utilizar a sua chave, crie um arquivo chamado _.env_ e utilize o modelo disponibilizado no arquivo _.env.example_, colocando a sua chave no lugar indicado. **O token deve estar dentro do arquivo _.env_ da mesma forma que está no arquivo _.env.example_**.
Exemplo: 
```
TOKEN = "ghp..."
```

4) Por fim, importe a RIT no seu arquivo fonte desta forma:
``` 
from BibliotecaRIT.Sources.BibliotecaRITFachada import  BibliotecaRITFachada
```

## **Método _calcularRelevanciaTematicaGitHub_**
A biblioteca dispõe de um único método a ser usado:
```
def calcularRelevanciaTematicaGitHub(self, usuario, repositorio, visao, autor , data)
```
Abaixo é descrito as informações necessárias para utilizar este método.
* No campo _usuario_ deve ser fornecido nome do dono do repositório que se deseja analisar a _issue_.
* No campo _repositorio_ deve ser fornecido o nome do repositório da _issue_ que será analisada.
* No campo _visao_ deve ser fornecido o tipo de filtro que será aplicado aos dados que serão exportados, sendo:  
    * 1 para filtrar por _issues_ abertas
    * 2 para filtrar por _issues_ fechadas
    * 3 para filtrar por _issues_ abertas e fechadas
    * 4 para filtrar comentários por autor
    * 5 para filtrar comentários por data
* No campo _autor_ deve ser fornecido o nome do autor que será utilizado para filtrar os comentários caso seja selecionado o filtro 4, caso contrário não precisa ser fornecido.
* No campo _data_ deve ser fornecido a data que será utilizada para filtrar os comentários caso seja selecionado o filtro 5, caso contrário não precisa ser fornecido. As datas devem ser fornecidas no formato yyyy-mm-dd.

Ao final da execução deste método é gerado um arquivos CSV que contém os seguintes dados acerca das _issues_ e seus comentários: ID da _issue_, título da _issue_, descrição da _issue_, data de criação da issue, ID do comentário, comentário, data do comentário, relevância Temática dos comentários e nome do autor do comentário

## **Exemplo**
No exemplo a seguir, será mostrado como utilizar a biblioteca RIT para calcular a relevância temática dos comentários do seguinte repositório: [https://github.com/mockturtl/dotenv](https://github.com/mockturtl/dotenv).
```
1 from Sources.BibliotecaRITFachada import BibliotecaRITFachada
2 # Instância da biblioteca
3 rit = BibliotecaRITFachada()
4 # Extrai e exporta em um arquivo CSV dados sobre as issues abertas do repositório dotenv do usuário mockturtl
5 # com a relevância temática dos comentários
6 rit.calcularRelevanciaTematicaGitHub(usuario="mockturtl",repositorio="dotenv",visao=1)
```
As linhas 4, 5, e 6 podem ser substituídas pelos códigos abaixo, variando com o tipo de filtro que é utilizado.

- Filtro 2
```
4 # Extrai e exporta em um arquivo CSV dados sobre as issues fechadas do repositório dotenv do usuário mockturtl
5 # com a relevância temática dos comentários
6 rit.calcularRelevanciaTematicaGitHub(usuario="mockturtl",repositorio="dotenv",visao=2)
``` 
- Filtro 3
```
4 # Extrai e exporta em um arquivo CSV dados sobre as issues abertas e fechadas do repositório dotenv do usuário mockturtl
5 # com a relevância temática dos comentários
6 rit.calcularRelevanciaTematicaGitHub(usuario="mockturtl",repositorio="dotenv",visao=3)
```  
- Filtro 4
```
4 # Extrai e exporta em um arquivo CSV dados sobre as issues abertas e fechadas do repositório dotenv do usuário mockturtl 
5 # com a relevância temática dos comentários que contém somente comentários do autor smayas
6 rit.calcularRelevanciaTematicaGitHub(usuario="mockturtl",repositorio="dotenv",visao=4,autor="smayas")
```
- Filtro 5
```
4 # Extrai e exporta em um arquivo CSV dados sobre as issues abertas e fechadas do repositório dotenv do usuário mockturtl
5 # com a relevância temática dos comentários que contém somente comentários na data 15/07/2021
6 rit.calcularRelevanciaTematicaGitHub(usuario="mockturtl",repositorio="dotenv",visao=5,data="2021-07-15")
```
### Saída
Ao executar o exemplo acima é gerado um arquivo CSV com o nome _dotenv.csv_, o qual contém os dados relacionados as _issues_ e a relevância temática dos comentários das issues.a