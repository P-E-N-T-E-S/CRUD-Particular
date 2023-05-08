import csv
import os
from Fpbiblioteca import * 
from time import sleep
os.system("cls")

while True:
    cabeçalho('MENU PRINCIPAL')
    resposta = menu(['Ler','CRUD','Encerrar'])
    if resposta == 1:
        print()
    elif resposta == 2:
        os.system("cls")
        resposta = menu(['Adição','Leitura', 'Atualização','Deleção'])
    else:
        break
    sleep(2)