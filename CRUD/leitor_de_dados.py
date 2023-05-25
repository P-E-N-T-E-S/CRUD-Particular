import os
from time import sleep

from Manipulacao_de_arquivos import manipulador_de_csv
from Formatacao.Formatacao_Menu import leiaInt


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
           list(str):retorna uma lista das categorias registradas no arquivo csv sem repetição.
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


def leitor_de_escolha_de_index(memoria_csv):
    '''Recebe como parâmetro uma matriz com todos os dados das transações e retorna a escolha(index) da transação
    que será alterado ou deletado.

        Parameters:
            memoria_csv (list):uma matriz com todos os dados das transações.

        Returns:
           int:retorna a escolha da transação(do index da transação) feita pelo usuário.
    '''
    while True:
        escolha = leiaInt('qual transação deseja alterar? (por index)')
        if not(escolha < 1):
            for linha in range(len(memoria_csv)):
                if memoria_csv[linha][0] == escolha:
                    print(f'{memoria_csv[linha][0]} - {memoria_csv[linha][1]}, {memoria_csv[linha][2]}, {memoria_csv[linha][3]}, {memoria_csv[linha][4]}, {memoria_csv[linha][5]}')
            return escolha
        else:
            print('\33[31mO numero 0 não é uma opção!\33[m')
            sleep(2)


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
            escolha = input(f"""Qual categoria você deseja visualizar? 
        entre: {categorias}
        --> """).lower()
            continuar = mostrador_de_resultado(categorias,escolha,memoria_csv)
            if not (continuar):
                break
        
        except(KeyboardInterrupt):
            print("\33[32mEscolha uma das categorias!\33[m")


def leitor_de_categoria(categorias):
    '''Recebe a lista de categorias computadas, e lê o input do do usuário, e, retona uma categoria nova
    válida ou uma existente.

        Args:
            categorias(list):uma lista das categorias existentes.

        Returns:
            str:retorna a categoria, ou a escolhida, ou uma nova.
    '''    
    while True:
        mensagem = f'escolha a categoria da transação:\nentre: {categorias}\nou digite [categoria] para adicionar uma nova categoria(sem virgula): '
        try:
            categoria = input(mensagem).lower()

            if categoria == 'categoria':
                categoria = input('digite a nova categoria: ').lower()

                if categoria.find(',') == -1:
                    return categoria
                else:
                    print('\33[31mInsira uma categoria válida(sem virgula)\33[m')
                    sleep(2)
            else:
                if categoria in categorias:
                    return categoria
                else:
                    print('\33[31mInsira uma categoria válida\33[m')
                    os.system('cls')
        except(KeyboardInterrupt):
            print("\33[31mEscolha uma das categorias!\33[m")


def mostrador_de_resultado(categorias,escolha,memoria_csv):
    '''Recebe como parâmetro 
     
       e espera um input de uma categoria existente a ser
    mostrada e retorna uma tabela, no terminal, filtrando apenas as transações da categoria escolhida.

        Parameters:
            lista_csv((str)list):linhas do arquivo csv sem nehuma formatação ou separação.
            categorias(list):uma lista das categorias existentes.
            escolha(str):a categoria escolhida para filtrar os resultados

        Returns:
           boll:retorna verdadeiro se essa sessão deve ser reiniciada no loop, retorna falso para voltar ao menu
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

