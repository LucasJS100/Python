def fatorial(num=1, Show=False):
    """

    ->Calcula o Fatorial de um número.
    :param num: O número a ser calculado
    :param Show: (Opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    """
    f = 1
    print('-'*25)
    for cont in range(num, 0, -1):
        if Show:
            print(f'{cont}', end=' X ' if cont > 1 else ' = ')
        f *= cont
    return f



print(fatorial(5, True))