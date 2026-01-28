def aumentar(num, prct, frmt=False):
    r = num + (num * (prct / 100))
    if frmt:
        formatado = 'R$' + f'{r:.2f}'.replace('.',',')
    return r

def diminuir(num, prct, frmt=False):
    r = num - (num * (prct / 100))
    if frmt:
        formatado = 'R$' + f'{r:.2f}'.replace('.',',')
    return r

def dobro(num, frmt=False):
    r = num * 2
    if frmt:
        formatado = 'R$' + f'{r:.2f}'.replace('.',',')
    return r

def metade(num, frmt=False):
    r = num / 2
    if frmt:
        formatado = 'R$' + f'{r:.2f}'.replace('.',',')
    return r

def moeda(num):
    formatado = f'R${num:.2f}'.replace('.',',')
    return formatado

def resumo(num, prct1, prct2):
    print('-'*30)
    print('       RESUMO DO VALOR')
    print('-'*30)
    formatado = 'R$' + f'{num:.2f}'.replace('.',',')
    print(f'Preço analisado:  {moeda(num)}')
    print(f'Dobro do preço:   {moeda(dobro(num))}')
    print(f'{prct1}% de aumento:   {moeda(aumentar(num, prct1))}')
    print(f'{prct2}% de redução:   {moeda(diminuir(num, prct2))}')
    print('-'*30)