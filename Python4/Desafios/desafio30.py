from rich import inspect, print

class Credencial():
    def __init__(self, hash):
        self.__hash = hash
    
    @property
    def senha(self):
        pass

    def validar(self, senha, chave):
        if chave == senha:
            print("Senha confere!")
            print("[green]True[/green]")
        else:
            print("Senha não bate!")
            print("[Red]False[/Red]")

c = Credencial()
c.senha = "Gafanhoto"

inspect(c, private=True, methods=True)