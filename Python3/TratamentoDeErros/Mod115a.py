from time import sleep
from Ex113 import *

def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[31mERROR: por favor , digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;32m{c}\033[m - \033[1;34m{item}\033[m')
        c += 1
    print(linha())
    op = leiaInt('Sua Opção: ')
    return op

'''def sistemaMenu():
    menu()
    try:
        op = int(input('\033[1;92mSua opção: \033[m'))
    except ValueError:
        print('\033[1;31mERRO: por favor, digite um número inteiro valido\033[m')
        sleep(1)
'''

def pessoaCadastro():
    cabeçalho('Opção 1')

def cadastradarPessoa():
    cabeçalho('Opção 2')

def sairSistema():
    cabeçalho('Saindo do sistema... Até logo!')


