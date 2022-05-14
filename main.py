from Sources.BibliotecaColMinerRTFachada import BibliotecaColMinerRTFachada

print('-------------------------------------------------------------------------------')
print('''                               MENU:
[1] - Processar Dados do GitHub
[2] - Processar Dados do StackOverflow
[3] - Sair ''')
opcao = int(input('Escolha uma Opção: '))
print('-------------------------------------------------------------------------------')
print()

if opcao == 1:
    usuario = input('[1] - Digite o Nome do Dono do Repositório: ')
    repositorio = input('[2] - Digite o Nome do Repositório: ')
    print()
    print('-------------------------------------------------------------------------------')
    print()
    
    print('''[1] - Issues Abertas
[2] - Issues Fechadas''')
    tipoIssue = int(input('Escolha uma Opção: '))
    print()
    print('-------------------------------------------------------------------------------')
    print()
    
    print('-- Processando Dados das Issues do Repositório --')
    projeto = BibliotecaColMinerRTFachada.processarDadosGitHub(usuario, repositorio, tipoIssue)
    print()
    
    print('-- Processando o Cálculo da Relevância Temática dos Comentários de Cada Issue --')
    BibliotecaColMinerRTFachada.calcularRelevanciaTematicaGitHub(projeto)
    print()
    
    print('-- Gerando o .csv com os Resultados Obtidos --')
    BibliotecaColMinerRTFachada.gerarCSVGitHub(projeto)
    print()
    
    print('-------------------------------------------------------------------------------')
    print()
    print('Obrigada(o) por usar a Biblioteca ColMiner RT!')
    print('Autores: Estela Miranda, Melissa Araújo, Fábio Trindade e Gláucia Braga')

elif opcao == 2:
    numero = input('[1] - Digite o Número do Tópico: ')
    idioma = input('[2] - Digite pt para Tópicos em Português, e en para Tópicos em Inglês: ')
    print()
    print('-------------------------------------------------------------------------------')
    print()
        
    print('-- Processando Dados do Tópico --')
    topico = BibliotecaColMinerRTFachada.processarDadosStackOverflow(numero, idioma)
    print()
        
    print('-- Processando o Cálculo da Relevância Temática dos Comentários de Cada Tópico --')
    BibliotecaColMinerRTFachada.calcularRelevanciaTematicaStackOverflow(topico)
    print()
        
    print('-- Gerando o .csv com os Resultados Obtidos --')
    BibliotecaColMinerRTFachada.gerarCSVStackOverflow(topico)
    print()
        
    print('-------------------------------------------------------------------------------')
    print()
    print('Obrigada(o) por usar a Biblioteca ColMiner RT!')
    print('Autores: Estela Miranda, Melissa Araújo, Fábio Trindade e Gláucia Braga')

else:
    print('Obrigada(o) por usar a Biblioteca ColMiner RT!')
    print('Autores: Estela Miranda, Melissa Araújo, Fábio Trindade e Gláucia Braga')