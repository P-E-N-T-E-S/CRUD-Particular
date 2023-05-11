def ler_ultimo_index(arq):
    with open(arq,'r') as arquivo:
        mensagem = arquivo.readlines()
        if len(mensagem) > 1:
            for linha in mensagem:
                ultima_linha = linha.split(',')
            return (int(ultima_linha[0]))
        else:
            return(0)

def adicionar(arq, ordem, data, hora):
    with open(arq, "a", encoding='utf-8', newline='') as arquivo:
        try:
            nome = input("Digite o nome da transação: ")
            while True:
                try:
                    categoria = input("Digite a categoria da transação: ")
                except ValueError():
                    print('\33[31mPor favor insira um valor válido\31[m')
                else:
                    break            
            valor = float(input("Digite o valor da transação: "))
            sinal = input('Você gastou ou recebeu esse dinheiro?(s/sim/recebi)ou(n/não/gastei)')
            if sinal.lower() in ['n','não', 'gastei']:
                valor = valor * -1
        except KeyboardInterrupt():
            print('\33[32mVoltando ao Menu...\33[m')
        else:
            arquivo.write(f"{ordem +1},{nome},{categoria},{valor},{data},{hora}\n")

def ler(arq):
    with open(arq, 'r', encoding='utf-8') as arquivo:
        memoria_csv = []
        arquivo_csv = arquivo.readlines()
        try:
            for linha in arquivo_csv:
                memoria_csv.append(linha.split(','))
            for c in memoria_csv:
                for a in range(len(c)):
                    print(c[a], end=' ')
                print('-'*54)
            input('digite enter para prosseguir')
        except:
            print('\33[31mErro inesperado, voltando ao menu\33[m')

def atualizar(arq):
    memoria_csv = []
    with open(arq, 'r',newline='', encoding='utf-8') as arquivo:
        arquivo_csv = arquivo.readlines()
        for linha in arquivo_csv:
            memoria_csv.append(linha.split(','))
    try:
        print('qual transação deseja alterar? (por index)')
        for c in memoria_csv:
                for a in range(len(c)):
                    print(c[a], end=' ')
                print('-'*54)
        escolha = input()
        for c in range(len(memoria_csv)):
                if memoria_csv[c][0] == escolha:
                    print(memoria_csv[c])
                    novonome = input('digite o novo nome da transação: ')
                    novacat = input('digite a nova categoria: ')
                    novovalor = float(input('digite o novo valor da transação '))
                    sinal = input('digite se foi um gasto ou ganho (s/sim/recebi)ou(n/não/gastei): ')
                    if sinal.lower() in ['n','não', 'gastei']:
                        novovalor = novovalor * -1
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
        print(memoria_csv)
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
        memoria_csv.pop(escolha+1)
    with open(arq, 'w', encoding='utf-8', newline='') as arquivo:
        arquivo.write('ordem,nome,categoria,valor,data,hora\n')
    with open(arq, 'a', encoding='utf-8', newline='') as arquivo:
        for c in memoria_csv:
            arquivo.write(f'{c}\n')
    

def ler_saldo_total(arq):
    with open(arq, 'r', encoding='utf-8') as arquivo:
        saldo = 0.0
        arquivo_csv = arquivo.readlines()
        arquivo_csv_dados = arquivo_csv[1:len(arquivo_csv)]
        try:
            for linha in arquivo_csv_dados:
                print(linha.split(',')[3])
                saldo += float(linha.split(',')[3])
            return saldo
        except:
            return '\33[31mErro\33[m'
        
