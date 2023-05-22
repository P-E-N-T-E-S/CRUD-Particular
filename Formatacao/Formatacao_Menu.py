def leiaInt(msg):
    '''essa função recebe como parametro uma mensagem a ser colocada no terminal, e vai pedir um numero como
    input, verifica se o input foi numero, se não for aparece uma mensagem de erro e pede novamente'''
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar um número.\033[m')
            return 0
        else:
            return num

def linha(tamanho = 42):
    '''Função responsável por printar linhas, para embelezamento dos menus.'''
    return "-" * tamanho

def cabeçalho(txt):
    '''Informe um texto; essa função vai transformar esse texto em um formato de menu centralizado'''
    print(linha())
    print(txt.center(42))
    print(linha())

def topicos(topicos):
    '''essa função recebe o input como lista e apresenta essa lista em formato de tópicos'''
    print()
    for topico in topicos:
        print(topico.ljust(42))
    print(linha())

def menu(list):
    '''Informe valores em forma de lista; essa função transforma a lista em formato de menu'''
    opcao = 1
    for item in list:
        print(f'\033[34m{opcao}\033[m - \033[34m{item}\033[m')
        opcao +=1
    print(linha())
    escolha = leiaInt('\033[32mSua Opção: \033[m')
    return escolha
