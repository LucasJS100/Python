from operacoes import *

while True:
    print("===== CALCULADORA =====")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    print("-"*25)

    escolha = int(input("Escolha uma opção: "))
    match escolha:
        case 1:
            quantos = int(input("Quantas vezes quer somar? "))
            numeros = []
            for i in range(quantos):
                somar = int(input(f"Escolha o {i+1}º número para somar: "))
                numeros.append(somar)

            print("-"*25)
            print(f"Resultado da soma: {soma(*numeros)}")
        case 2:
            quantos = int(input("Quantas vezes quer subtrair? "))
            numeros = []
            for i in range(quantos):
                subtrair = int(input(f"Escolha o {i+1}º número para somar: "))
                numeros.append(subtrair)
            print("-"*25)
            print(f"Resultado da subtração: {subtração(*numeros)}")
        case 3:
            quantos = int(input("Quantas vezes quer fazer uma multiplicar? "))
            numeros = []
            for i in range(quantos):
                multiplicar = int(input(f"Escolha o {i+1}º número para multiplicar: "))
                numeros.append(multiplicar)
            print("-"*25)
            print(f"Resultado da subtração: {multiplicacao(*numeros)}")
        case 4:
            quantos = int(input("Quantas vezes quer fazer uma divisão? "))
            numeros = []
            for i in range(quantos):
                dividir = int(input(f"Escolha o {i+1}º número para dividir: "))
                numeros.append(dividir)
            print("-"*25)
            print(f"Resultado da subtração: {divisao(*numeros)}")
        case 5:
            print('Saindo...')
            break