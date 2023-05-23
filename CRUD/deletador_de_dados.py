from CRUD import atualizador_de_dados as atualizador

from Manipulacao_de_arquivos import manipulador_de_csv


def deletar(arq):
    '''Recebe como parâmetro nome do arquivo csv de banco de dados, depois mostra todas as linhas do arquivo e espera
    a resposta de qual transação deve ser deletada(por index), após isso reescreve o arquivo sem a transação escolhida
    atualizando o index.

    Parameters:
        arq(str):nome do arquivo csv de banco de dados.

    Raises:
        ValueError:
    '''
    memoria_csv = manipulador_de_csv.conversor_de_csv_em_lista(arq)
    escolha = atualizador.leitor_de_escolha_de_index(memoria_csv)
    memoria_csv.pop(escolha)

    with open(arq, 'w', encoding='utf-8', newline='') as arquivo:
        arquivo.write('ordem,nome,categoria,valor,data,hora\n')

    with open(arq, 'a', encoding='utf-8', newline='') as arquivo:
        nova_ordem = 0
        for linha in memoria_csv:
            if linha[0] != 'ordem':
                novaordem += 1
                linha[0] = str(nova_ordem)
                linhaformat = ','.join(linha)
                arquivo.write(f'{linhaformat}\n')
