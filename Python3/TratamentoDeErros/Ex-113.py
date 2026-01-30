def leiaInt(num):
    ok = False
    valor = 0
    while True:
        try:
            n = str(input(num)).strip()
            if n.isnumeric():
                valor = int(n)
                ok = True
        except ValueError:
            print('ERROR: por favor , digite um número inteiro válido.')
        if ok:
            break
    return valor
def leiaFloat(num):
    ok = False
    valor = 0
    while True:
        try:
            n = str(input(num))
            if n.isnumeric():
                valor = float(n)
                ok = True
        except ValueError:
            print('ERROR: por favor , digite um número real válido.')
        if ok:
            break
    return valor

i = leiaInt("Digite um Inteiro: ")
r = leiaFloat('Digite um Real: ')

print(f'O valor inteiro digitado foi {i} e o real foi {r}.')