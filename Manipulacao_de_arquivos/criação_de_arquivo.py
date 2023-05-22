from time import sleep
def conferirarquivo(nome):
    '''função que verifica a existência do arquivo para salvar os dados, tentando abrir o arquivo através do try except,
    se no try ele conseguir abiri o arquivo ele retorna verdadeiro se ele não existir então o except retornará falso.'''
    existencia = True
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        existencia = False
    return(existencia)

def criararquivo():
    '''função que retorna o nome do arquivo para salvar dados, se ele existir, ou cria um arquivo, se ele não existir'''
    nome = 'controle.csv'
    existencia = conferirarquivo(nome)
    if not existencia:
        print('\33[31mArquivo de salvamento não existente, criando arquivo...\33[m')
        with open(nome, 'w') as arquivo:
            arquivo.write('Ordem,Nome,Categoria,Valor,Data,Hora\n')
            sleep(1)
        print('\33[32mArquivo de salvamento  controle.csv criado, com sucesso\33[m')
    else:
        print('\33[32mEncontrado arquivo de salvamento controle.csv\33[m')
    return(nome)
