from Mod115a import *

while True:
    resposta = menu(['Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        pessoaCadastro()
        sleep(1)
    elif resposta == 2:
        cadastradarPessoa()
        sleep(1)
    elif resposta == 3:
        sairSistema()
        break
    else:
        print('\033[1;31mERRO: Digite uma opção válida!\033[m')
        sleep(1)