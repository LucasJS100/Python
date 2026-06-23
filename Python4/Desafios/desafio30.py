from rich import inspect, print
from hashlib import sha256

class Credencial():
    def __init__(self, hash='', senha=''):
        self.senha = senha
        self.__hash = hash
    
    @property
    def senha(self, senha):
        self.__hash = sha256(self.senha.encode('utf-8'))
        return self.__hash__

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