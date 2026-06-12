from rich import inspect, print
from getpass import getpass

class ContaBancaria():
    def __init__(self, id, nome, saldo, chave=None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        self.__hash = chave
        print(f"Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:,}")
        if chave == None:
            self.pede_senha()
    
    @property
    def nome(self):
        return self._titular

    def depositar(self, valor):
        self.__saldo += valor
        print(f"Deposito de R${valor:.2f} autorizado na conta {self._id}")

    def pede_senha(self) -> str:
        return getpass("Senha: ")

    def sacar(self, valor:float, chave:str = None):
        if chave is None:
            chave = self.pede_senha()

        if chave == self.__hash:
            if valor <= self.__saldo:
                self.__saldo -= valor
                print(f"Saque de R${valor:.2f} autorizado na conta {self._id}")
            else:
                print("Saque não realizado. Valor mais alto que o no saldo.")
        else:
            print("Senha não confere. Saque não autorizado!")


    def validar_senha(self, chave:str) -> bool:
        ...
    
print("Criando a conta...")
cc = ContaBancaria(123, "Gustavo", 1000, "Gafanhoto")

print("Realizando depósito")
cc.depositar(500)

print("Realizando saque")
cc.sacar(200)

#inspect(cc, private=True, methods=True)