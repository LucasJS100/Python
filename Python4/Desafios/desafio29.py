from rich import inspect, print

class Diario():
    def __init__(self, senha):
        self.__segredos = []
        self.__senha = senha.strip()

    @property
    def senha(self):
        raise PermissionError("Ninguem tem permissão de ver a senha")
    
    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())

    def ler(self, senha=None):
        if senha == self.__senha:
            print("[bold green]Diário LIBERADO![/bold green]")
            for i in self.__segredos:
                print(f"- {i}")
        else:
            raise PermissionError("Senha inválida! Você não pode ler meu diário!")

d = Diario("Gafanhoto")
d.escrever("Primeira Mensagem")
d.escrever("Você é uma pessoa simpática")
d.escrever("Você gosta de Python")

d.ler("Gafanhoto")
