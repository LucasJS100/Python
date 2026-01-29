from utilidadescev.moeda import resumo
from utilidadescev.dado import leiaDinheiro


p = leiaDinheiro('Digite o preço: R$')
resumo(p, 35, 22)

'''
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
'''
