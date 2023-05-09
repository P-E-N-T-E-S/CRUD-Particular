
def conferirarquivo():
    existencia = True
    try:
        a = open('controle.csv', 'rt')
        a.close()
    except:
        print('\33[31mArquivo não existente, criando arquivo...\33[m')
        existencia = False
    return(existencia)

def criararquivo():
    existencia = conferirarquivo()
    nome = 'controle.csv'
    if not existencia:
        with open(nome, 'w') as arquivo:
            arquivo.write('ordem,nome,categoria,valor,data,hora\n')
        print('\33[32mArquivo controle.csv criado, com sucesso\33[m')
    else:
        print('Encontrado arquivo controle.csv')
    return(nome)
