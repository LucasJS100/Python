from rich import inspect, print

class Diario():
    def __init__(self, senha):
        self.__segredos = []
        self.__senha = senha

    @property
    def senha(self):
        raise PermissionError("Ninguem tem permissão de ver a senha")
    
    def escrever(self, msg):
        self.__segredos.append(msg)

    def ler(self, senha=None):
        if senha == self.__senha:
            print("[green]Diário LIBERADO![green]")
            for i in self.__segredos:
                print(f"- {i}")
        else:
            print("Senha Incorreta")

d = Diario("Gafanhoto")
d.escrever("Primeira Mensagem")
d.escrever("Você é uma pessoa simpática")
d.escrever("Você gosta de Python")

d.ler("Gafanhoto")
