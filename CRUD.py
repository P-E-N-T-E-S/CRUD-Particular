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
        try:
            categoria = input("Digite a categoria da transação: ")
            while True:
                try:
                    valor = float(input("Digite o valor da transação: "))
                except ValueError():
                    print('\33[31mPor favor insira um valor válido\31[m')
                else:
                    break
            nome = input("Digite o nome da transação: ")
        except KeyboardInterrupt():
            print('\33[32mVoltando ao Menu...\33[m')
        else:
            arquivo.write(f"\n{ordem +1},{nome},{categoria},{valor},{data},{hora}")

def ler(arq):
    with open(arq, 'r', encoding='utf-8') as arquivo:
        memoria_csv = []
        arquivo_csv = csv.reader(arquivo, delimiter = ',')
        try:
            for linha in arquivo_csv:
                memoria_csv.append(linha)
            for c in memoria_csv:
                for a in range(len(c)):
                    print(c[a].ljust(9), end=' ')
                print()
            input('digite enter para prosseguir')
        except:
            print('\33[31mErro inesperado, voltando ao menu\33[m')

def atualizar(arq):
    memoria_csv = []
    with open(arq, 'r',newline='', encoding='utf-8') as arquivo:
        arquivo_csv = csv.reader(arquivo)
        for linha in arquivo_csv:
            memoria_csv.append(linha)
    try:
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
                    novovalor = float(input('digite o novo valor da transação '))
                    while True:
                        try:
                            memoria_csv[c][1] = novonome
                            memoria_csv[c][2] = novacat
                            memoria_csv[c][3] = novovalor
                        except ValueError():
                            print('\33[31mPor favor insira um valor válido\31[m')
                        else:
                            break
                    print(memoria_csv[c])
    except KeyboardInterrupt():
        print('\33[32mVoltando ao Menu...\33[m')
    else:
        with open(arq, 'w', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo, delimiter= ',')
            for i in memoria_csv:
                writer.writerow(i)

def deletar(arq):
    memoria_csv = []
    with open(arq, 'r',newline='', encoding='utf-8') as arquivo:
        arquivo_csv = csv.reader(arquivo)
        for linha in arquivo_csv:
            memoria_csv.append(linha)
        print('qual transação deseja deletar? (por index)')
        for c in memoria_csv:
            for a in range(len(c)):
                print(c[a].ljust(9), end=' ')
            print()
        while True:
            try:
                escolha = int(input())
            except ValueError():
                    print('\33[31mPor favor insira um valor válido\31[m')
            else:
                break
        for c in range(len(memoria_csv)):
                if memoria_csv[c][0] == str(escolha):
                    memoria_csv.pop(c)