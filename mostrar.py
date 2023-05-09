import os
os.system('cls')
categoria = []

with open('controle.csv', 'r', encoding='utf-8') as arquivo:
    lista_csv = arquivo.readlines()
    escolha = input("Qual categoria você deseja vizualizar? ").lower()
    if escolha in ['casa','lazer','trabalho']:
        for l in lista_csv:
            l = l.split(',')
            if l[0] == 'ordem':
                print("ordem  nome  categoria  valor  data  hora")
            for a in range(len(l)):
                if l[2] == escolha:
                    print(l[a], end='\t')
            if l[2] == escolha:
                print()
    else:
        print("Essa categoria não existe, digite uma categoria válida")