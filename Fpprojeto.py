import csv
import os
from Fpbiblioteca import * 
from time import sleep
import CRUD as crud
import criação_de_arquivo as ca
os.system("cls")
arq = ca.criararquivo()
while True:
    os.system('cls')
    cabeçalho('MENU')
    resposta = menu(['Ler','Alterar','Encerrar'])
    if resposta == 1:
        crud.ler(arq)
    elif resposta == 2:
        while True:
            os.system("cls")
            print(linha())
            resposta = menu(['Adição', 'Atualização','Deleção', 'Voltar'])
            if resposta == 1:
                crud.adicionar(arq, index, data=, hora=)
            elif resposta == 2:
                print()
            elif resposta == 3:
                print()
            elif resposta == 4:
                print('\033[32mVoltando...\033[m')
                break
            else:
                print('\033[31mERRO: por favor, digite uma das opções.\033[m')
            sleep(2)
    elif resposta == 3:
        break
    else:
        print('\033[31mERRO: por favor, digite uma das opções.\033[m')
    sleep(2)

