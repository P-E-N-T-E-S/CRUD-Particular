import csv

def ler_ultimo_index(arq):
    with open(arq,'r') as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter = ',')
        ultima_linha = []
        for linha in arquivo_csv:
            ultima_linha = linha
    return int(ultima_linha[0])

def adicionar(arq, ordem, data, hora):
    with open(arq, "a") as arquivo:
            categoria = input("Digite a categoria da transação: ")
            valor = float(input("Digite o valor da transação: "))
            nome = input("Digite o nome da transação: ")
            arquivo.write(f"\n{ordem +1},{nome},{categoria},{valor},{data},{hora}")

def ler(arq):
    with open(arq, 'r', encoding='utf-8') as arquivo:
        memoria_csv = []
        arquivo_csv = csv.reader(arquivo, delimiter = ',')
        for linha in arquivo_csv:
            memoria_csv.append(linha)
        for c in memoria_csv:
            for a in range(len(c)):
                print(c[a].ljust(9), end=' ')
            print()
        input('digite enter para prosseguir')

def atualizar(arq):
    memoria_csv = []
    with open(arq, 'r',newline='', encoding='utf-8') as arquivo:
        arquivo_csv = csv.reader(arquivo)
        for linha in arquivo_csv:
            memoria_csv.append(linha)
        print(memoria_csv)
    print('qual transação deseja alterar? (por index)')
    for c in memoria_csv:
        for a in range(len(c)):
            print(c[a].ljust(9), end=' ')
        print()
    escolha = input()
    for c in range(len(memoria_csv)):
            if memoria_csv[c][0] == escolha:
                print(memoria_csv[c])
                novonome = input('digite o novo nome da transação: ')
                novacat = input('digite a nova categoria: ')
                novovalor = input('digite o novo valor da transação ')
                memoria_csv[c][1] = novonome
                memoria_csv[c][2] = novacat
                memoria_csv[c][3] = novovalor
                print(memoria_csv[c])
    with open(arq, 'w', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo, delimiter= ',')
        for i in memoria_csv:
            writer.writerow(i)