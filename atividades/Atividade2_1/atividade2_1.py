lista_pessoas = []

def dadosPessoa(nome='', cidade=''):
    listaDados = {
        "nome": nome,
        "cidade": cidade
    }
    lista_pessoas.append(listaDados)
    
def listarCadastros():
    for i in lista_pessoas:
        print(f"Nome: {i['nome']} | Cidade: {i['cidade']}")


def buscarCadastro(procurarNome):
    for a in lista_pessoas:
        if a['nome'].lower() == procurarNome.lower():
            return f"O nome {procurarNome} está na lista: Nome: {a['nome']} | Cidade: {a['cidade']}"
    return f"O nome {procurarNome} não foi encontrado."
