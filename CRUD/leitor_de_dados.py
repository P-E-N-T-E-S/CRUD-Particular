from Manipulacao_de_arquivos import manipulador_de_csv


def ler(arq):
    '''Recebe como parametro o nome do arquivo csv de banco de dados em que mostrara no terminal linha a linha
    formatado como tabela. Tendo formatações especiais dependendo do valor de cada posição, como nas posições
    de valores em que adiciona o prefixo 'R$' na frente, ao fim espera qualquer input do usuário.

        Parameters:
            arq(str):nome do arquivo csv de banco de dados.
    '''    
    memoria_csv = []
    memoria_csv = manipulador_de_csv.conversor_de_csv_em_lista(arq)
    for linha in memoria_csv:
        for palavra in range(len(linha)):
            if palavra == 3 and linha != 0:
                print(f'R${linha[palavra]}', end=' ')
            else:
                print(linha[palavra].ljust(12), end=' ')
        print()
    input('digite enter para prosseguir')



def ler_saldo_total(arq):
    '''Recebe como parametro o nome do arquivo csv de banco de dados que filtra apenas os valores das transações
    e soma todos os ganhos e perdas nas transações e retorna o balanço geral.

        Parameters:
            arq(str):nome do arquivo csv de banco de dados.
        
        Raises:
            AttributeError:se ocorrer algum errro inesperado tenta reiniciar o menu.
            KeyboardInterrupt:se houver algum input inesperado do usuário no meio da operação retorna ao menu.
            ValueError:se houver algum erro na operação interrope ela
    '''
    memoria_csv = []
    saldo = 0.0
    memoria_csv = manipulador_de_csv.conversor_de_csv_em_lista(arq='controle.csv')
    print()
    try:
        for linha in memoria_csv:
            print(linha)
            if linha[3] != 'valor':
                saldo += float(linha[3])
        return(saldo)
    except:
        print(saldo)
        print('\33[31mErro inesperado, reinicie o programa ou contate os devs\33[m')
        



def ler_ultimo_index(arq):
    '''Recebe como parametro o nome do arquivo csv de banco de dados em que ela vai procurar na posição do numero da
    transação(index 0) o numero da ultima transação e o retornar, caso não haja transação ele retorna 0.

        Parameters:
            arq(str):nome do arquivo csv de banco de dados.

        Returns:
           (int):retorna o numero do ultimo numero de transação, se não houver retorna 0.
    '''
    memoria_csv = []
    memoria_csv = manipulador_de_csv.conversor_de_csv_em_lista(arq)
    if len(memoria_csv) > 1:
        ultima_linha = memoria_csv[len(memoria_csv)-1]
        return (int(ultima_linha[0]))
    else:
        return(0)



def achar_categoria(arq):
    '''Recebe como parâmetro nome do arquivo csv de banco de dados filtrando apenas os valores de categorias das 
    transações(index 2) e retorna uma lista com as categorias sem repetição.

        Parameters:
            arq(str):nome do arquivo csv de banco de dados.
        
        Raises:
            AttributeError:se houver algum erro inesperado na manipulação do arquivo volta ao menu.

        Returns:
           (list):retorna uma lista das categorias registradas no arquivo csv sem repetição.
    '''
    categorias = []
    memoria_csv = []
    memoria_csv = manipulador_de_csv.conversor_de_csv_em_lista(arq)
    try:
        for linha in memoria_csv:
            categorias.append(linha[2])
        categorias = list(set(categorias))
        categorias.remove('categoria')
        return(categorias)
    except:
        print('\33[31mErro inesperado, reinicie o programa ou contate os devs\33[m')



def ler_filtrado_por_categoria(arq):
    '''Recebe como parâmetro nome do arquivo csv de banco de dados e espera um input de uma categoria existente a ser
    mostrada e mostra uma tabela, no terminal, filtrando apenas as transações da categoria escolhida.

        Parameters:
            arq(str):nome do arquivo csv de banco de dados.
        
        Raises:
            KeyboardInterrupt:se houver algum input inesperado do usuário reinicia a função.
    '''
    categorias = achar_categoria(arq)
    memoria_csv = manipulador_de_csv.conversor_de_csv_em_lista(arq)
    while True:
        try:
            escolha = input(f"""Qual categoria você deseja vizualizar? 
        entre: {categorias}
        --> """).lower()
            continuar = mostrador_de_resultado(categorias,escolha,memoria_csv)
            if not (continuar):
                break
        
        except(KeyboardInterrupt):
            print("\33[32mEscolha uma das categorias!\33[m")



def mostrador_de_resultado(categorias,escolha,memoria_csv):
    '''Recebe como parâmetro 
     
       e espera um input de uma categoria existente a ser
    mostrada e retorna uma tabela, no terminal, filtrando apenas as transações da categoria escolhida.

        Parameters:
            lista_csv((str)list):linhas do arquivo csv sem nehuma formatação ou separação.
            categorias(list):uma lista das categorias existentes.
            escolha(str):a categoria escolhida para filtrar os resultados

        Returns:
           (boll):retorna verdadeiro se essa sessão deve ser reiniciada no loop, retorna falso para voltar ao menu
    '''
    if escolha in categorias:
        for linha in memoria_csv:
            if linha[0] == 'ordem':
                print('ordem'.ljust(12), 'nome'.ljust(12), 'categoria'.ljust(12), 'valor'.ljust(12), 'data'.ljust(12), 'hora')
            for index in range(len(linha)):
                if linha[2] == escolha:
                    print(linha[index].ljust(12), end='')
            if linha[2] == escolha:
                print()
        input('digite enter para continuar')
        return False
    elif escolha.lower() == 'sair' or escolha.lower() == 's':
        return False
    else:
        print("Essa categoria não existe, digite uma categoria válida, ou digite 'sair' ou 's' para voltar ao menu:")
        return True

