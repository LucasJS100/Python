from abc import ABC, abstractmethod
from rich import print
from rich.table import Table
from rich.console import Console

console = Console()

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0
    
    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, distancia, fator=0.50):
        super().__init__(distancia)
        self.fator = fator

    def calc_frete(self):
        #Frete livre
        self.frete = self.distancia * self.fator

        return f"R${self.frete}"


class Caminhao(Transporte):
    def __init__(self, distancia, fator=1.20):
        super().__init__(distancia)
        self.fator = fator

    def calc_frete(self):
        #minimo 50km
        self.frete = self.distancia * self.fator

        if self.distancia >= 50:
            return f"R${self.frete}"
        else:
            return "Raio mínimo de 50Km"

class Drone(Transporte):
    def __init__(self, distancia, fator=9.50):
        super().__init__(distancia)
        self.fator = fator

    def calc_frete(self):
        #maximo 10km
        self.frete = self.distancia * self.fator
        if self.distancia < 10:
            return f"R${self.frete}"
        else:
            return "Raio máximo de 10Km"


dist = 80

entrega = Drone(dist)
viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

# print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.calc_frete()}")

tabela = Table(title="Tabela de Fretes")

tabela.add_column("Distancia")
tabela.add_column("Tipo")
tabela.add_column("Frete")

for item in viagem:
    tabela.add_row(f"{dist}Km", f"{type(item).__name__}", f"{item.calc_frete()}")

print(tabela)