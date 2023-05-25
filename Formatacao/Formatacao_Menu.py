def leiaInt(msg):
    '''Recebe como parametro uma mensagem a ser colocada no terminal, e pede um numero como input,
    verifica se o input pode ser convertido para int, se não for mostra uma mensagem de erro e pede novamente.

        Parameters:
            msg(str):mensagem que será mostrada no terminal.
        
        Raises:
            ValueError,TypeError:se a função receber algo não convertivel para int.
            KeyboardInterrupt:se o programa for interrompido pelo usuário.
               
        Returns:
           int:em caso de nenhuma escolha retorna 0.\n
           int:se a operação ocorreu com sucesso retona o numero esperado.
        
    '''
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


def leiaFloat(msg):
    '''Recebe como parametro uma mensagem a ser colocada no terminal, e pede um numero como input,
    verifica se o input pode ser convertido para float, se não for mostra uma mensagem de erro e pede novamente.

        Parameters:
            msg(str):mensagem que será mostrada no terminal.
        
        Raises:
            ValueError,TypeError:se a função receber algo não convertivel para int.
            KeyboardInterrupt:se o programa for interrompido pelo usuário.
               
        Returns:
           float:em caso de nenhuma escolha retorna 0.\n
           float:se a operação ocorreu com sucesso retona o numero esperado.
        
    '''
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar um número.\033[m')
            return 0
        else:
            return num


def linha(tamanho = 42):
    '''Função responsável por printar linhas, para formatação dos menus.

        Parameters:
            tamanho(int):tamanho da linha para formatação, por padrão valor 42.
        Returns:
           str:retorna a linha para formatação.
    '''
    return "-" * tamanho


def cabeçalho(txt):
    '''Transforma um texto em um formato de menu centralizado.

        Parameters:
            txt(str):texto do menu a ser formatado.
    '''
    print(linha())
    print(txt.center(42))
    print(linha())


def topicos(topicos):
    '''Recebe o input como lista e apresenta essa lista em formato de tópicos usando um for e formatando todos os topicos.

        Parameters:
            topicos(list):lista de topicos para serem mostrados no menu.
    '''
    print()
    for topico in topicos:
        print(topico.ljust(42))
    print(linha())


def menu(sessoes):
    '''Recebe as opções do menu em forma de listade strings e transforma a lista em formato do menu além de receber o
    input do usuário e retornando a opção escolhida.

        Parameters:
            sessoes(list):lista de opções do menu que guiaram a cada tela.
        Returns:
           int:retorna a opção escolhida pelo usuário.
    '''
    opcao = 1
    for item in sessoes:
        print(f'\033[34m{opcao}\033[m - \033[34m{item}\033[m')
        opcao +=1
    print(linha())
    escolha = leiaInt('\033[32mSua Opção: \033[m')
    return escolha
