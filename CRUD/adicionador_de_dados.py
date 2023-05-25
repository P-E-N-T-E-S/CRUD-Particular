from time import sleep
from CRUD import leitor_de_dados as leitor
from Formatacao.Formatacao_Menu import leiaFloat


def verificador_de_cancelamento():
    '''Verifica se o usuário deseja cancelar a operação, atraves da verificação do input do usuário.

        Returns:
           bool:retorna verdadeiro se o usuário digitou ok, do contrário retorna falso.
    '''
    while True:
        cancelamento_input = input('digite [ok] para prosseguir ou [cancelar] para não registrar: ').lower()
        if cancelamento_input not in ['ok' , 'cancelar']:
            print('\33[31mDigite uma resposta válida\33[m')
        else:
            if cancelamento_input == 'ok' or cancelamento_input == 'prosseguir':
                return True
            else:
                return False 


def classificador_de_valor(valor):
    '''Recebe o valor da transação e apartir da escolha do usuário converte para um gasto(negativo) ou ganho(positivo).
        Parameters:
            valor (int):O valor da transação.

        Returns:
           int:retorna o valor convertido para o sinal desejado.
    '''
    situacao = input('Você gastou ou recebeu esse dinheiro?[Recebi] ou [Gastei]: ')
    if situacao.lower() in ['gastei']:
        valor = valor * -1
    return valor

def verificador_de_input_valido(msg):
    valor = input(msg)
    if valor.find(',') == -1:
        return valor
    else:
        print('\33[31mValor Inválido indentificado: virgula(,)\33[m')
        sleep(0.5)
        print('\33[32mSubstituindo virgula(,) por ifem(-)\33[m')
        sleep(2)
        return valor.replace(',','-')

def adicionar(arq, ordem, data, hora):
    '''Recebe como parâmetro nome do arquivo csv de banco de dados e algumas informações da transação, e adiciona as
    informações os inputs do usuario para criar uma nova transação e registrar ela no arquivo.

    Parameters:
        arq (str):nome do arquivo csv de banco de dados.
        ordem (int):posição da ultima transação.
        data (str):data da transação
        hora (str):hora da transação

    Raises:
        KeyboardInterrupt:se o usuário digitar algo no meio da operação interrompe a função.
    '''
    categorias = leitor.achar_categoria(arq)
    nome = verificador_de_input_valido("Digite o nome da transação: ")
    try:
        categoria_da_transação = leitor.leitor_de_categoria(categorias)
        valor = leiaFloat("Digite o valor da transação: ")
        valor = classificador_de_valor(valor)
        print(f"a nova transação será: {ordem +1},{nome},{categoria_da_transação},{valor}0,{data},{hora}")
        cancelamento = verificador_de_cancelamento()
        if cancelamento:
            with open(arq, "a", encoding='utf-8', newline='') as arquivo:
                arquivo.write(f"{ordem +1},{nome},{categoria_da_transação},{valor}0,{data},{hora}\n")
        else:
            print('\33[32mVoltando ao Menu...\33[m')

    except (KeyboardInterrupt):
        print('\33[32mVoltando ao Menu...\33[m')