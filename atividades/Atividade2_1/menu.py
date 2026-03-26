from atividade2_1 import *

while True:
    print("~"*30)
    print("-----------CADASTRO-----------")
    print("1 - Cadastrar")
    print("2 - Listar Cadastrados")
    print("3 - Buscar por Nome")
    print("4 - Sair")
    print("~"*30)

    escolha = int(input("Escolha uma opção: "))
    match escolha:
        case 1:
            nome = str(input("Digite um nome: "))
            cidade = str(input("Digite a cidade: "))
            infoPessoa(nome, cidade)
        case 2:
            exibirCadastros()
        case 3:
            procurar = str(input("Digite o nome que quer procurar: "))
            print(verificarNome(procurar))
        case 4:
            print("Desligando...")
            break