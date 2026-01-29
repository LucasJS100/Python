def aumentar(preco=0, taxa=0, frmt=False):
    r = preco + (preco * (taxa / 100))
    return r if not frmt else moeda(r)

def diminuir(preco=0, taxa=0, frmt=False):
    r = preco - (preco * (taxa / 100))
    return r if not frmt else moeda(r)

def dobro(preco=0, frmt=False):
    r = preco * 2
    return r if not frmt else moeda(r)

def metade(preco=0, frmt=False):
    r = preco / 2
    return r if not frmt else moeda(r)

def moeda(preco=0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(preco=0, taxa1=10, taxa2=5):
    print('-'*30)
    print('       RESUMO DO VALOR')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa1}% de aumento: \t{aumentar(preco, taxa1, True)}')
    print(f'{taxa2}% de redução: \t{diminuir(preco, taxa2, True)}')
    print('-'*30)