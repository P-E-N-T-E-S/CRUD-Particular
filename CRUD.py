import csv
def adicionar(arq):
    with open(arq, "a") as arquivo:
            categoria = input("Digite a categoria da transação: ")
            valor = float(input("Digite o valor da transação: "))
            oque = input("Digite o nome da transação: ")
            writer = csv.writer(arquivo, delimiter=',')
            writer.writerow(['\n', oque, categoria, valor])
            #arquivo.write(f"{categoria};{valor};{oque}")

def ler(arq):
    with open(arq, "r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=",")
        for linha in arquivo_csv:
            print(linha)
        input('digite enter para voltar')

def atualizar():
    memoria_csv = []
    with open('Controle.CSV', 'r') as arquivo:
        arquivo_csv = csv.reader(arquivo)
        for linha in arquivo_csv:
            memoria_csv.append(linha[0].split(','))
    print('qual transação deseja alterar? (por index)')
    for c in memoria_csv:
        for a in range(len(c)):
            print(c[a].ljust(9), end=' ')
        print()
    escolha = input()
    for c in range(len(memoria_csv)):
        if memoria_csv[c] == escolha:
            memoria_csv.pop(c)
            novonome = input('digite o novo nome da transação: ')
            novacat = input('digite a nova categoria: ')
            novovalor = input('digite o novo valor da transação ')
            memoria_csv.insert(c, [novonome, novacat, novovalor])
    with open('Controle.CSV', 'w') as arquivo:
        writer = csv.writer(arquivo, delimiter= ',')
        for i in memoria_csv:
            writer.writerow(i)


def ler2(arq):
    with open(arq, 'r') as arquivo:
        memoria_csv = []
        arquivo_csv = csv.reader(arquivo, delimiter = ',')
        for linha in arquivo_csv:
            memoria_csv.append(linha[0].split(','))
        print(memoria_csv)


