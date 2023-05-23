import os
from Manipulacao_de_arquivos import vizualizador_de_dados 

def adicionar(arq, ordem, data, hora):
    '''Recebe como parâmetro nome do arquivo csv de banco de dados e algumas informações da transação, e adiciona as
    informações os inputs do usuario para criar uma nova transação e registrar ela no arquivo.

    Parameters:
        arq(str):nome do arquivo csv de banco de dados.
        ordem(int):posição da ultima transação.
        data(str):data da transação
        hora(str):hora da transação

    Raises:
        AttributeError:
        KeyboardInterrupt:
    '''
    with open(arq, "a", encoding='utf-8', newline='') as arquivo:
        categorias = vizualizador_de_dados.achar_categoria(arq)
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



def atualizar(arq):
    '''Recebe como parâmetro nome do arquivo csv de banco de dados e mostra todo o arquivo em formato de tabela,
    esperando do usuário a escolha de qual linha será atualizada, atualizando todas as informações exceto:
    index,data e hora.

    Parameters:
        arq(str):nome do arquivo csv de banco de dados.

    Raises:
        AttributeError:
        ValueError:
    '''
    categorias = vizualizador_de_dados.achar_categoria(arq)
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
    '''Recebe como parâmetro nome do arquivo csv de banco de dados, depois mostra todas as linhas do arquivo e espera
    a resposta de qual transação deve ser deletada(por index), após isso reescreve o arquivo sem a transação escolhida
    atualizando o index.

    Parameters:
        arq(str):nome do arquivo csv de banco de dados.

    Raises:
        ValueError:
    '''
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
