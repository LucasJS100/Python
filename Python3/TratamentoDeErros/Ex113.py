def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except:
            print('ERROR: por favor , digite um número inteiro válido.')
            continue
        else:
            return n

def leiaFloat(num):
    while True:
        try:
            n = float(input(num))
        except:
            print('ERROR: por favor , digite um número real válido.')
            continue 
        else:
            return n

i = leiaInt("Digite um Inteiro: ")
r = leiaFloat('Digite um Real: ')

print(f'O valor inteiro digitado foi {i} e o real foi {r}.')