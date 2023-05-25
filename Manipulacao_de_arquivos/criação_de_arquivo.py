from time import sleep


def conferirarquivo(nome): 
    '''Verifica a existencia do arquivo csv para salvar os dados das transações.

        Parameters:
            nome(str):nome do arquivo a ser vertificado.

        Raises:
            AttributeError: se houver falha em abrir o arquivo muda o valor da variável existencia para False.

        Returns:
           bool:retorna verdadeiro se o arquivo com esse nome existe.
    '''

    existencia = True
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        existencia = False
    return(existencia)


def criararquivo():
    '''Retorna o nome do arquivo para salvar dados, se ele existir, ou cria um arquivo, se ele não existir

        Returns:
           str:retorna, depois da verificação de existência, o nome do arquivo csv de banco de dados.
    '''
    nome = 'controle.csv'
    existencia = conferirarquivo(nome)
    if not existencia:
        print('\33[31mArquivo de salvamento não existente, criando arquivo...\33[m')
        with open(nome, 'w') as arquivo:
            arquivo.write('ordem,nome,categoria,valor,data,hora\n')
            sleep(1)
        print('\33[32mArquivo de salvamento  controle.csv criado, com sucesso\33[m')
    else:
        print('\33[32mEncontrado arquivo de salvamento controle.csv\33[m')
    return(nome)
