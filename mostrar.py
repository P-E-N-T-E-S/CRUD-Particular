import csv
import os
os.system('cls')
categoria = []

with open('controle.csv', 'r', encoding='utf-8') as arquivo:
    lista_csv = csv.reader(arquivo, delimiter= ',')
    escolha = input("Qual categoria você deseja vizualizar? ").lower()
    print("Essa categoria não existe, digite uma categoria válida")
    for l in lista_csv:
        if l[0] == 'ordem':
            print("ordem  nome  categoria  valor  data  hora")
        for a in range(len(l)):
            if l[2] == escolha:
                print(l[a], end='\t')
        if l[2] == escolha:
            print('')
