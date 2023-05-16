import os
nome_do_arquivo_de_teste = 'controle.csv'

if not(os.path.exists(nome_do_arquivo_de_teste)):
    with open(nome_do_arquivo_de_teste,'x') as arquivo_de_teste:
        memoria_csv =[
                    'ordem,nome,categoria,valor,data,hora\n',
                    '1,sorvete,lazer,10.5,03/05/2023,17:17:25\n',
                    '2,encanamento,casa,400.0,10/05/2023,12:15:00\n',
                    '3,salvavidas,casa,500.0,20/04/2023,09:30:17\n',
                    '4,cafe,lazer,10.0,02/05/2023,05:13:25\n',
                    '5,Pizza,lazer,45.0,08/05/2023,16:13:25\n',
                    '6,argamassa,casa,150.0,09/05/2023,09:46:19\n'
                    ]
        arquivo_de_teste.writelines(memoria_csv)
else: 
    print('Controle já existe')