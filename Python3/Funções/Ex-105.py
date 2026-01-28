def notas(*notas, sit=False):
    """
    notas(*notas, sit=False)
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma
    """
    dicioNotas = {}
    dicioNotas['total'] = len(notas)
    dicioNotas['maior'] = max(notas)
    dicioNotas['menor'] = min(notas)
    dicioNotas['média'] = sum(notas) / len(notas)
    if sit:
        if dicioNotas['média'] >= 7:
            dicioNotas['situação'] = 'BOA'
        elif dicioNotas['média'] >=5:
            dicioNotas['situação'] = 'RAZOAVEL'
        else:
            dicioNotas['situação'] = 'RUIM'
    return dicioNotas
        

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)