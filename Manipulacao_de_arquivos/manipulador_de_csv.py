def conversor_de_csv_em_lista(arq):
    '''Recebe como parametro o nome do arquivo csv de banco de dados e localiza o arquivo, e o converte para
    uma matriz com todos os valores.

        Parameters:
            arq(str):nome do arquivo csv de banco de dados.
        
        Raises:
            AttributeError:
            KeyboardInterrupt:
            ValueError:
        Returns:
           list:retorna uma matriz dos valores do arquivo csv
    '''
    memoria_csv = []
    try:
        with open(arq, 'r',newline='', encoding='utf-8') as arquivo:
            arquivo_csv = arquivo.readlines()
            for linha in arquivo_csv:
                memoria_csv.append(linha.split(','))
            for linha in memoria_csv:
                for palavra in range(len(linha)):
                    linha[palavra] = linha[palavra].strip()
            return memoria_csv
    except:
        print('\33[31mErro ao carregar arquivo de banco de dados,\nSe o problema persistir reinicie o programa e contate os devs \33[m')
