import criação_de_arquivo as ca
import csv
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
        arquivo.write('ordem,nome,categoria,valor,data,hora')
    with open(arq, 'w', encoding='utf-8', newline='') as arquivo:
        for c in memoria_csv:
            arquivo.write(f'{c}\n')
    
ca.criararquivo()
deletar('controle2.csv')