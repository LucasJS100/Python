c = ('\033[m',          # 0 - sem cores
    '\033[0;30;41m'     # 1 - vermelho
    '\033[0;30;42m',    # 2 - verde
    '\033[0;30;43m',    # 3 - amarelo
    '\033[0;30;44m',    # 4 - azul
    '\033[0;30;45m',    # 5 - roxo
    '\033[7;30m',       # 6 -branco
    );

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')

def título(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~'* tamanho)
    print(f'  {msg}')
    print('~'* tamanho)
    print(c[0], end='')

comando = ''

while True:
    título('SISTEMA DE AJUDA PYHELP', 1)
    comando = str(input("Função Ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)