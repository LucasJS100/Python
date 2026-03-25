def soma(*a):
    total = 0
    for numero in a:
        total += numero
    return total

def subtração(*a):
    resultado = a[0]
    for num in a[1:]:
        resultado -= num
    return resultado

def multiplicacao(*a):
    resultado = a[0]
    for num in a[1:]:
        resultado *= num
    return resultado

def divisao(*a):
    resultado = a[0]
    for num in a[1:]:
        resultado /= num
    return resultado
