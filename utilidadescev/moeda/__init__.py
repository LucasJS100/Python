from utilidadescev import dado

def moeda(num):
    formatado = 'R$' + f'{num:.2f}'.replace('.',',')
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