import os
from Manipulacao_de_arquivos import manipulador_de_csv
os.system('cls')
memoria_csv = []
saldo = 0.0
memoria_csv = manipulador_de_csv.conversor_de_csv_em_lista(arq='controle.csv')
print()
try:
    for linha in memoria_csv:
        print(linha)
        if linha[3] != 'valor':
            saldo += float(linha[3])
            print(saldo)
except:
    print(saldo)
    print('\33[31mErro inesperado, reinicie o programa ou contate os devs\33[m')