def acharcat(arq):
    '''essa função recebe como parâmetro o caminho do arquivo que ela vai procurar no index 2 que está registrados as 
    categorias das transações e nos retorna uma lista com as categorias sem repetição'''
    categorias = []
    try:
        with open(arq, 'r', newline='', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                valores = linha.split(',')
                categorias.append(valores[2])
            categorias = list(set(categorias))
            categorias.remove('Categoria')
            return(categorias)
    except:
        print('\33[31mErro inesperado, reinicie o programa ou contate os devs\33[m')

def ler_ultimo_index(arq):
    '''essa função recebe como parametro o caminho do arquivo em que ela vai procurar no index 0 o numero da ultima transação e
    retorna ele caso não haja transação ele retorna 0'''
    with open(arq,'r') as arquivo:
        mensagem = arquivo.readlines()
        if len(mensagem) > 1:
            for linha in mensagem:
                ultima_linha = linha.split(',')
            return (int(ultima_linha[0]))
        else:
            return(0)

def adicionar(arq, ordem, data, hora):
    '''essa função recebe como parametros o caminho do arquivo, a posição da ultima transação a data e a hora local e vai receber
    inputs do usuario para criar uma nova transação e registrar ela no arquivo'''
    import os
    with open(arq, "a", encoding='utf-8', newline='') as arquivo:
        categorias = acharcat(arq)
        try:
            nome = input("Digite o nome da transação: ")
            while True:
                categoria = input(f'''escolha a categoria da transação:
    entre: {categorias}
    ou digite [categoria] para adicionar uma nova categoria: ''')
                if categoria == 'categoria':
                    categoria = input('digite a nova categoria: ').title()
                    break
                else:
                    if categoria in categorias:
                        break
                    else:
                        print('\33[31mInsira uma categoria válida\33[m')
                        os.system('cls')
                        continue
            while True:
                try:
                    valor = float(input("Digite o valor da transação: "))
                except:
                    print('\33[31mPor favor insira um valor válido\33[m')
                else:
                    break
            situacao = input('Você gastou ou recebeu esse dinheiro?[Recebi] ou [Gastei]: ')
            if situacao.lower() in ['gastei']:
                valor = valor * -1
            print(f"a nova transação será: {ordem +1},{nome},{categoria},{valor}0,{data},{hora}")
            while True:
                cancelamento = input('digite [ok] para prosseguir ou [cancelar] para não registrar: ').lower()
                if cancelamento not in ['ok' , 'cancelar']:
                    print('\33[31mDigite uma resposta válida\33[m')
                else:
                    break
        except (KeyboardInterrupt):
            print('\33[32mVoltando ao Menu...\33[m')
        else:
            if cancelamento == 'ok':
                arquivo.write(f"{ordem +1},{nome},{categoria},{valor}0,{data},{hora}\n")
            else:
                print('\33[32mVoltando ao Menu...\33[m')

def ler(arq):
    '''essa função recebe como parâmetro o nome do arquivo csv em que ela vai mostrar no terminal linha a linha formatado como tabela,
    quando chega no index 5 ela coloca um R$ na frente, para terminar a função ela espera um enter'''

    memoria_csv = []
    with open(arq, 'r',newline='', encoding='utf-8') as arquivo:
            arquivo_csv = arquivo.readlines()
            for linha in arquivo_csv:
                memoria_csv.append(linha.split(','))
            for linha in memoria_csv:
                for palavra in range(len(linha)):
                    linha[palavra] = linha[palavra].strip()
            for linha in memoria_csv:
                for palavra in range(len(linha)):
                    if palavra == 3 and linha != 0:
                        print(f'R${linha[palavra]}', end=' ')
                    else:
                        print(linha[palavra].ljust(12), end=' ')
                print()
            input('digite enter para prosseguir')


def atualizar(arq):
    '''essa função recebe como parâmetro o nome do arquivo e mostra todo o arquivo em formato de tabela, assim ela espera uma
    resposta do usuário para escolher qual linha do arquivo será alterada, a função vai pedir inputs para trocar o nome a 
    categoria e o valor da transação, mantendo o index, a data e a hora'''
    categorias = acharcat(arq)
    memoria_csv = []
    with open(arq, 'r',newline='', encoding='utf-8') as arquivo:
        arquivo_csv = arquivo.readlines()
        for linha in arquivo_csv:
            memoria_csv.append(linha.split(','))
    try:
        print('qual transação deseja alterar? (por index)')
        for linha in memoria_csv:
            for palavra in range(len(linha)):
                linha[palavra] = linha[palavra].strip()
        for linha in memoria_csv:
            for palavra in range(len(linha)):
                if palavra == 3 and linha != 0:
                    print(f'R${linha[palavra]}'.ljust(12), end=' ')
                else:
                    print(linha[palavra].ljust(12), end=' ')
            print()
        escolha = input('   -->')
        for linha in range(len(memoria_csv)):
                if memoria_csv[linha][0] == escolha:
                    print(f'{memoria_csv[linha][0]} - {memoria_csv[linha][1]}, {memoria_csv[linha][2]}, {memoria_csv[linha][3]}, {memoria_csv[linha][4]}, {memoria_csv[linha][5]}')
                    novonome = input('digite o novo nome da transação: ')
                    while True:
                        novacat = input(f'''escolha a categoria da transação:{categorias}
    ou digite [categoria] para adicionar uma nova categoria: ''')
                        if novacat == 'categoria':
                            novacat = input('digite a nova categoria: ')
                            addcat = True
                            break
                        else:
                            addcat = False
                            if novacat in categorias:
                                break
                            else:
                                print('\33[31mInsira uma categoria válida\33[m')
                                continue
                    novovalor = float(input('digite o novo valor da transação '))
                    sinal = input('digite se foi um gasto ou ganho (s/sim/recebi)ou(n/não/gastei): ')
                    if sinal.lower() in ['n','não', 'gastei']:
                        novovalor = novovalor * -1
                    while True:
                        try:
                            memoria_csv[linha][1] = novonome
                            memoria_csv[linha][2] = novacat
                            memoria_csv[linha][3] = f'{novovalor}0'
                        except ValueError():
                            print('\33[31mPor favor insira um valor válido\31[m')
                        else:
                            break
                    print(f'a transação ficou: {memoria_csv[linha][0]} - {memoria_csv[linha][1]}, {memoria_csv[linha][2]}, {memoria_csv[linha][3]}, {memoria_csv[linha][4]}, {memoria_csv[linha][5]}')
                    prosseguir = input('para confirmar pressione [enter] ou insira [cancelar] para cancelar: ').upper()
    except:
        print('\33[31mVoltando ao Menu...\33[m')
    else:
        if prosseguir != 'cancelar':
            with open(arq, 'w', encoding='utf-8') as arquivo:
                arquivo.write('ordem,nome,categoria,valor,data,hora\n')
            with open(arq, 'a', encoding='utf-8') as arquivo:
                for linha in range(1, len(memoria_csv)):
                    arquivo.write(f'{memoria_csv[linha][0]},{memoria_csv[linha][1]},{memoria_csv[linha][2]},{memoria_csv[linha][3]},{memoria_csv[linha][4]},{memoria_csv[linha][5].strip()}\n')
                    print('\33[31mTransação atualizada!\33[m')
        else:
            print( '\33[31mCancelando operação... \33[m')

def deletar(arq):
    '''essa função recebe como parâmetro o caminho do arquivo, ela vai mostrar todas as linhas do arquivo
    em formatação de tabela e vai perguntar qual transação deve ser deletada por index, após isso reescreeve
    o arquivo sem a transação escolhida e refazendo o index'''
    memoria_csv = []
    with open(arq, 'r',newline='', encoding='utf-8') as arquivo:
        arquivo_csv = arquivo.readlines()
        for linha in arquivo_csv:
            memoria_csv.append(linha.split(','))
        for linha in memoria_csv:
            for palavra in range(len(linha)):
                linha[palavra] = linha[palavra].strip()
        print('qual transação deseja deletar? (por index)')
        for linha in memoria_csv:
            for palavra in range(len(linha)):
                print(linha[palavra].ljust(12), end=' ')
            print()
        while True:
            try:
                escolha = int(input())
            except(ValueError):
                    print('\33[31mPor favor insira um valor válido\33[m')
            else:
                break
        memoria_csv.pop(escolha)
    with open(arq, 'w', encoding='utf-8', newline='') as arquivo:
        arquivo.write('ordem,nome,categoria,valor,data,hora\n')
    with open(arq, 'a', encoding='utf-8', newline='') as arquivo:
        novaordem = 0
        for linha in memoria_csv:
            if linha[0] != 'ordem':
                novaordem += 1
                linha[0] = str(novaordem)
                linhaformat = ','.join(linha)
                arquivo.write(f'{linhaformat}\n')
            else:
                continue
        
def ler_saldo_total(arq):
    '''essa função recebe como parâmetro o caminho do arquivo e ela analisa toda a coluna 5 para
    calcular todos os ganhos e perdas nas transações e retorna como valor float o balanço geral'''
    try:
        with open(arq, 'r', encoding='utf-8') as arquivo:
            saldo = 0.0
            arquivo_csv = arquivo.readlines()
            arquivo_csv_dados = arquivo_csv[1:len(arquivo_csv)]
            try:
                for linha in arquivo_csv_dados:
                    saldo += float(linha.split(',')[3])
                return(saldo)
            except:
                return('\33[31mErro\33[m')
    except(KeyboardInterrupt):
        print('\33[31mVoltando ao menu\33[m')
    except:
        print('\33[31mErro inesperado, reinicie o programa ou contate os devs\33[m')
        
def mostrarcat(arq):
    '''essa função recebe como função o caminho do arquivo e pede como input uma categoria a ser mostrada
    então ela mostra o arquivo com formatação de tabela filtrando para aparecer apenas as transações da
    categoria escolhida'''
    categorias = acharcat(arq)
    with open(arq, 'r', encoding='utf-8') as arquivo:
        lista_csv = arquivo.readlines()
        while True:
            try:
                escolha = input(f"""Qual categoria você deseja vizualizar? 
            entre: {categorias}
            --> """).lower()
                if escolha in categorias:
                    for l in lista_csv:
                        l = l.split(',')
                        if l[0] == 'ordem':
                            print('ordem'.ljust(12), 'nome'.ljust(12), 'categoria'.ljust(12), 'valor'.ljust(12), 'data'.ljust(12), 'hora')
                        for a in range(len(l)):
                            if l[2] == escolha:
                                print(l[a].ljust(12), end='')
                        if l[2] == escolha:
                            print()
                    input('digite enter para continuar')
                    break
                elif escolha.lower() == 'sair' or escolha.lower() == 's':
                    break
                else:
                    print("Essa categoria não existe, digite uma categoria válida, ou digite 'sair' ou 's' para voltar ao menu:")
            except(KeyboardInterrupt):
                print("\33[32mEscolha uma das categorias!\33[m")