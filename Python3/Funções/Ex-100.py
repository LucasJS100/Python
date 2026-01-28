from random import randint
from time import sleep
lista = []

def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(5):
        numero = randint(1, 10)
        lista.append(numero)
        print(f'{numero} ', end='', flush=True)
        #sleep(0.3)
    print('PRONTO!')

def somaPar():
    num = 0
    for index in lista:
        if index % 2 == 0:
            num += index
   # sleep(1)
    print(f'Somando os valores pares de {lista} temos {num}.')

sorteia()
somaPar()