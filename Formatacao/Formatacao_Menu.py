def leiaInt(msg):
    '''Essa função é usada para tratamento de erro; assim a opção selecionado só será aceita se for dentro das opções'''
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def linha(tam = 42):
    '''Coloca algumas linhas'''
    return "-" * tam

def cabeçalho(txt):
    '''Informe um texto; essa função vai transformar esse texto em um formato de menu centralizado'''
    print(linha())
    print(txt.center(42))
    print(linha())

def topicos(topicos):
    print()
    for topico in topicos:
        print(topico.ljust(42))
    print(linha())

def menu(list):
    '''Informe valores em forma de lista; essa função transforma a lista em formato de menu'''
    c = 1
    for item in list:
        print(f'\033[34m{c}\033[m - \033[34m{item}\033[m')
        c +=1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc
