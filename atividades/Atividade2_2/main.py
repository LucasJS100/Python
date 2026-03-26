from operacoes import *

while True:
    print("=== CALCULADORA SIMPLES ===")
    print("1- Soma")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")
    print("5- Sair")
    
    escolha = int(input("Escolha uma opção: "))

    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print("-" * 25)

    if escolha == 1:
        print(f"Resultado: {soma(n1, n2)}")
    elif escolha == 2:
        print(f"Resultado: {subtracao(n1, n2)}")
    elif escolha == 3:
        print(f"Resultado: {multiplicacao(n1, n2)}")
    elif escolha == 4:
        if n2 != 0:
            print(f"Resultado: {divisao(n1, n2)}")
        else:
            print("Erro: Não é possível dividir por zero!")
    elif escolha == 5:
        print("Saindo....")
        break
    else:
        print("Erro, Tente Novamente.")
    print("-" * 25)
