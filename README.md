# **Biblioteca ColMiner para Cálculo de Relevância Temática**

O projeto ColMiner tem como objetivo analisar dados de ambientes de issue tracking com o intuito de apoiar o gerenciamento das comunicações em projetos de software. Para isso, a principal métrica utilizada nas análises é a relevância temática dos comentários postados nas issues associada a outras medidas quantitativas que possam revelar possíveis falhas de comunicação.

<br>

## **🟣 Sobre a Biblioteca ColMiner**

A Biblioteca de Relevância Temática faz parte dos refinamentos e extensões da ferramenta ColMiner, em que suas macro-funcionalidades serão modularizadas e estendidas. Essa biblioteca analisa os comentários postados no ambiente de issue tracking do GitHub e nos tópicos de discussão do StackOverflow, por meio do cálculo da Relevância Temática dos mesmos, ou seja, calcula-se quão relevantes os comentários são para uma discussão. Através da Biblioteca, é possível:

<br>

* Calcular o quão relevante é cada comentário para o tema da discussão de uma issue no GitHub; e
* Calcular o quão relevante é cada resposta para o tema da discussão de um tópico do StackOverflow, podendo também indicar o mais relevante.
* Extrair os Dados calculados dos comentários através do formato CSV.

<br>

## **🟢 Instalação**

Como a biblioteca foi desenvolvida de forma a pensar no minímo possível de dependências com bibliotecas externas, existe apenas uma biblioteca que deve ser instalada, a [Stack API](https://stackapi.readthedocs.io/en/latest/), usada para extrair os dados da plataforma do StackOverflow. Dessa forma, i criado um arquivo, ```requirements.txt``` que irá instalar todas as dependências necessárias, bastando apenas ter instalado o [pip](https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/), após isso, basta executar o comando:

```
pip3 install -r requirements.txt
```