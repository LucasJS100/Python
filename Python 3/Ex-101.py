from datetime import date

anoAtual = date.today().year

def voto(ano):
    idade = anoAtual - ano
    if idade >= 18 and idade < 65:
        return 'VOTO OBRIGATÓRIO'
    elif idade >= 16 and idade < 18 or idade >= 65:
        return 'VOTO OPICIONAL'
    else:
        return 'NÃO VOTA'

pergunta = int(input(f'Em que ano você nasceu? '))
print(f'Com {anoAtual-pergunta} anos: {voto(pergunta)}')