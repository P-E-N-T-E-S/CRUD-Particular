import os
from time import sleep
import datetime as date

from Formatacao.Formatacao_Menu import * 
import Manipulacao_de_arquivos.criação_de_arquivo as ca

import CRUD.leitor_de_dados as leitor
import CRUD.adicionador_de_dados as escritor
import CRUD.atualizador_de_dados as atualizador
import CRUD.deletador_de_dados as deletador


os.system("cls")
arq = ca.criararquivo()

while True:
    saldo = leitor.ler_saldo_total(arq)
    sleep(1)
    os.system('cls')
    cabeçalho('MENU')
    topicos([f'Saldo: R$ {saldo}'])
    resposta = menu(['Ler','Alterar','Encerrar'])
    
    if resposta == 1:#vizualizar transações
        while True:
            os.system('cls')
            print(linha())
            resposta2 = menu(['Mostrar tudo', 'Mostrar por categoria', 'Voltar'])
            if resposta2 == 1:
                leitor.ler(arq)
                sleep(1)
            elif resposta2 == 2:
                leitor.ler_filtrado_por_categoria(arq)
                sleep(1)
            elif resposta2 == 3:
                break
            sleep(1)
    elif resposta == 2:
        while True:
            os.system("cls")
            print(linha())
            resposta = menu(['Adição', 'Atualização','Deleção', 'Voltar'])
            if resposta == 1:
                escritor.adicionar(arq,ordem = leitor.ler_ultimo_index(arq) ,data= date.datetime.now().strftime('%d/%m/%Y'), hora= date.datetime.now().strftime('%X'))
            elif resposta == 2:
                atualizador.atualizar(arq)
            elif resposta == 3:
                deletador.deletar(arq)
            elif resposta == 4:
                print('\033[32mVoltando...\033[m')
                break
            else:
                print('\033[31mERRO: por favor, digite uma das opções.\033[m')
            sleep(1)
    elif resposta == 3:
        break
    else:
        print('\033[31mERRO: por favor, digite uma das opções.\033[m')