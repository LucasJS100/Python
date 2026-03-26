from operacoes import *

while True:
    print("=== CALCULADORA SIMPLES ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    
    escolha = int(input("Escolha uma opção: "))
    match escolha:
        case 1:
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
            print(f"Resultado: {soma(n1, n2)}")
        case 2:
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
            print(f"Resultado: {subtracao(n1, n2)}")
        case 3:
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
            print(f"Resultado: {multiplicacao(n1, n2)}")
        case 4:
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
            if n2 != 0:
                print(f"Resultado: {divisao(n1, n2)}")
            else:
                print("Erro: Não é possível dividir por zero!")
    print("-" * 30)
