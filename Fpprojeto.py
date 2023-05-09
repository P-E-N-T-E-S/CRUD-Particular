import os
from Fpbiblioteca import * 
from time import sleep
import CRUD as crud
import criação_de_arquivo as ca
import datetime as date
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
                crud.adicionar(arq,ordem = crud.ler_ultimo_index(arq) ,data= date.datetime.now().strftime('%d/%m/%Y'), hora= date.datetime.now().strftime('%X'))
            elif resposta == 2:
                crud.atualizar(arq)
            elif resposta == 3:
                crud.deletar(arq)
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

