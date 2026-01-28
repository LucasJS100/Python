def voto(ano):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - ano
    if idade >= 18 and idade < 65:
        return f'Com {anoAtual-pergunta} anos: VOTO OBRIGATÓRIO'
    elif idade >= 16 and idade < 18 or idade >= 65:
        return f'Com {anoAtual-pergunta} anos: VOTO OPICIONAL'
    else:
        return f'Com {anoAtual-pergunta} anos: NÃO VOTA'

pergunta = int(input(f'Em que ano você nasceu? '))
print(voto(pergunta))