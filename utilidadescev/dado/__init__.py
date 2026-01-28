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