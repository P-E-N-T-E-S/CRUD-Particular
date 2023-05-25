from CRUD import leitor_de_dados as leitor
from CRUD import adicionador_de_dados as adicionador

from Manipulacao_de_arquivos import manipulador_de_csv
from Formatacao.Formatacao_Menu import leiaInt, leiaFloat

from time import sleep

def reescritor_de_arquivo(arq,memoria_csv):
    '''Recebe como parâmetro nome do arquivo csv de banco de dados e uma matriz com todos os dados de todas as 
    transações salvas, e com esses dados reescreve todo o banco de dados com as novas informações atualizadas.

    Parameters:
        arq(str):nome do arquivo csv de banco de dados.
        memoria_csv (list):uma matriz com todos os dados das transações.
    '''    
    with open(arq, 'w', encoding='utf-8') as arquivo:
        arquivo.write('ordem,nome,categoria,valor,data,hora\n')
    with open(arq, 'a', encoding='utf-8') as arquivo:
        for linha in range(1, len(memoria_csv)):
            arquivo.write(f'{memoria_csv[linha][0]},{memoria_csv[linha][1]},{memoria_csv[linha][2]},{memoria_csv[linha][3]},{memoria_csv[linha][4]},{memoria_csv[linha][5].strip()}\n')
        print('\33[32mTransação atualizada!\33[m')
        sleep(2)


def atualizar(arq):
    '''Recebe como parâmetro nome do arquivo csv de banco de dados e mostra todo o arquivo em formato de tabela,
    esperando do usuário a escolha de qual linha será atualizada, atualizando todas as informações exceto:
    index,data e hora.

    Parameters:
        arq(str):nome do arquivo csv de banco de dados.

    Raises:
        AttributeError:
        ValueError:
    '''
    categorias = leitor.achar_categoria(arq)
    memoria_csv = manipulador_de_csv.conversor_de_csv_em_lista(arq)
    leitor.ler(arq)
    ordem_de_transacao = leitor.leitor_de_escolha_de_index(memoria_csv)
    novo_nome = input('digite o novo nome da transação: ')
    nova_categoria = leitor.leitor_de_categoria(categorias)
    novo_valor = leiaFloat('digite o novo valor da transação: ')
    novo_valor = adicionador.classificador_de_valor(novo_valor)
    try:
        try:
            memoria_csv[ordem_de_transacao][1] = novo_nome
            memoria_csv[ordem_de_transacao][2] = nova_categoria
            memoria_csv[ordem_de_transacao][3] = f'{novo_valor:.2f}'
        except ValueError():
            print('\33[31mPor favor insira um valor válido\31[m')

        print(f'a transação ficou: {memoria_csv[ordem_de_transacao][0]} - {memoria_csv[ordem_de_transacao][1]}, {memoria_csv[ordem_de_transacao][2]}, {memoria_csv[ordem_de_transacao][3]}, {memoria_csv[ordem_de_transacao][4]}, {memoria_csv[ordem_de_transacao][5]}')
        continuar = adicionador.verificador_de_cancelamento()
        
        if continuar:
            reescritor_de_arquivo(arq,memoria_csv)
        else:
            print('\33[31mCancelando operação... \33[m')
    except:
        print('\33[31mVoltando ao Menu...\33[m')
        

