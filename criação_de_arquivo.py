
def conferirarquivo():
    existencia = True
    try:
        a = open('controle.csv', 'rt')
        a.close()
    except:
        print('\33[31marquivo não existente, criando arquivo...\33[m')
        existencia = False
    return(existencia)
def criararquivo():
    import csv
    existencia = conferirarquivo()
    if not existencia:
        with open('controle.csv', 'w') as arquivo:
            writer = csv.writer(arquivo, delimiter=',')
            writer.writerow(['ordem', 'nome', 'categoria', 'valor'])
        print('\33[32marquivo controle.csv criado, com sucesso\33[m')
    else:
        print('encontrado arquivo controle.csv')
