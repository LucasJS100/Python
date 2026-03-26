listadaspessoas = []

def infoPessoa(nome='', cidade=''):
    listaDados = {
        "nome": nome,
        "cidade": cidade
    }
    listadaspessoas.append(listaDados)
    
def exibirCadastros():
    for i in listadaspessoas:
        print(f"Nome: {i['nome']} | Cidade: {i['cidade']}")


def verificarNome(buscarNome):
    for a in listadaspessoas:
        if a['nome'].lower() == buscarNome.lower():
            return f"O nome {buscarNome} está na lista: Nome: {a['nome']} | Cidade: {a['cidade']}"
    return f"O nome {buscarNome} não foi encontrado."
