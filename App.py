import os
from Formatacao.Formatacao_Menu import * 
from time import sleep
import Manipulacao_de_arquivos.CRUD as crud
import Manipulacao_de_arquivos.criação_de_arquivo as ca
import datetime as date


os.system("cls")
arq = ca.criararquivo()

while True:
    saldo = crud.ler_saldo_total(arq)
    os.system('cls')
    cabeçalho('MENU')
    topicos([f'Saldo: R$ {saldo}'])
    resposta = menu(['Ler','Alterar','Encerrar'])
    
    if resposta == 1:
        while True:
            os.system('cls')
            print(linha())
            resposta2 = menu(['Mostrar tudo', 'Mostrar por categoria', 'Voltar'])
            if resposta2 == 1:
                crud.ler(arq)
                sleep(2)
            elif resposta2 == 2:
                crud.mostrarcat(arq)
                sleep(2)
            elif resposta2 == 3:
                break
            sleep(2)
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
    #sleep(2)
