def ler_ultimo_index(arq):
    with open(arq,'r') as arquivo:
        mensagem = arquivo.readlines()
        if len(mensagem) > 1:
            for linha in mensagem:
                ultima_linha = linha.split(',')
            return (int(ultima_linha[0]))
        else:
            return(0)

def adicionar(arq, ordem, data, hora, categorias):
    with open(arq, "a", encoding='utf-8', newline='') as arquivo:
        try:
            nome = input("Digite o nome da transação: ")
            while True:
                categoria = input(f'''escolha a categoria da transação:
        {categorias}
        ou digite [categoria] para adicionar uma nova categoria: ''')
                if categoria == 'categoria':
                    novacat = input('digite a nova categoria: ')
                    addcat = True
                    break
                else:
                    addcat = False
                    if not categoria in categorias:
                        print('\33[31mPor favor insira uma categoria válida!\33[m')
                    else:
                        break
            valor = float(input("Digite o valor da transação: "))
        except KeyboardInterrupt():
            print('\33[32mVoltando ao Menu...\33[m')
        else:
            if addcat:
                arquivo.write(f"{ordem +1},{nome},{novacat},{valor},{data},{hora}\n")
            else:
                arquivo.write(f"{ordem +1},{nome},{categoria},{valor},{data},{hora}\n")

def ler(arq):
    try:
        memoria_csv = []
        with open(arq, 'r',newline='', encoding='utf-8') as arquivo:
            arquivo_csv = arquivo.readlines()
            for linha in arquivo_csv:
                memoria_csv.append(linha.split(','))
            for a in memoria_csv:
                for c in range(len(a)):
                    a[c] = a[c].strip()
            for c in memoria_csv:
                for a in range(len(c)):
                    print(c[a].ljust(12), end=' ')
                print()
            input('digite enter para prosseguir')
    except:
        print('\33[31mErro inesperado, voltando ao menu\33[m')

def atualizar(arq):
    memoria_csv = []
    with open(arq, 'r',newline='', encoding='utf-8') as arquivo:
        arquivo_csv = arquivo.readlines()
        for linha in arquivo_csv:
            memoria_csv.append(linha.split(','))
        for a in memoria_csv:
                for c in range(len(a)):
                    a[c] = a[c].strip()
    try:
        print('qual transação deseja alterar? (por index)')
        for c in memoria_csv:
            for a in range(len(c)):
                print(c[a].ljust(12), end=' ')
        escolha = input()
        for c in range(len(memoria_csv)):
                if memoria_csv[c][0] == escolha:
                    print(memoria_csv[c])
                    novonome = input('digite o novo nome da transação: ')
                    novacat = input('digite a nova categoria: ')
                    memoria_csv[c][1] = novonome
                    memoria_csv[c][2] = novacat
                    while True:
                        try:
                            novovalor = float(input('digite o novo valor da transação '))
                        except ValueError:
                            print('\33[31mPor favor insira um valor válido\31[m')
                        else:
                            break
                    memoria_csv[c][3] = novovalor
                    print(memoria_csv[c])
    except KeyboardInterrupt():
        print('\33[32mVoltando ao Menu...\33[m')
    else:
        with open(arq, 'w', encoding='utf-8') as arquivo:
            arquivo.write('ordem,nome,categoria,valor,data,hora\n')
        with open(arq, 'a', encoding='utf-8') as arquivo:
            for c in range(1, len(memoria_csv)):
                arquivo.write(f'{memoria_csv[c][0]},{memoria_csv[c][1]},{memoria_csv[c][2]},{memoria_csv[c][3]},{memoria_csv[c][4]},{memoria_csv[c][5].strip()}\n')

def deletar(arq):
    memoria_csv = []
    with open(arq, 'r',newline='', encoding='utf-8') as arquivo:
        arquivo_csv = arquivo.readlines()
        for linha in arquivo_csv:
            memoria_csv.append(linha.split(','))
        for a in memoria_csv:
            for c in range(len(a)):
                a[c] = a[c].strip()
        print('qual transação deseja deletar? (por index)')
        for c in memoria_csv:
            for a in range(len(c)):
                print(c[a].ljust(12), end=' ')
            print()
        while True:
            try:
                escolha = int(input())
            except ValueError():
                    print('\33[31mPor favor insira um valor válido\31[m')
            else:
                break
        memoria_csv.pop(escolha+1)
    with open(arq, 'w', encoding='utf-8', newline='') as arquivo:
        arquivo.write('ordem,nome,categoria,valor,data,hora\n')
    with open(arq, 'a', encoding='utf-8', newline='') as arquivo:
        reordem = 0
        for c in memoria_csv:
            if c[0] != 'ordem':
                reordem += 1
                c[0] = str(reordem)
                a = ','.join(c)
                arquivo.write(f'{a}\n')
            else:
                continue

def acharcat():
    categorias = []
    with open('controle.csv', 'r', newline='', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            valores = linha.split(',')
            categorias.append(valores[2])
        for a in range(len(categorias)):
            for b in range(a+1, len(categorias)):
                if categorias[a] == categorias[b]:
                    del categorias[b]
    del categorias[0]
    return(categorias)
