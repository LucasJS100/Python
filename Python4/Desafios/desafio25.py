from abc import ABC, abstractmethod
from rich.table import Table
from rich.console import Console

console = Console()

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        frete = 0
    
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


dist = 8

entrega = Drone(dist)
viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

# print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.calc_frete()}")

table = Table(title="Tabela de Fretes")

table.add_column("Distancia", justify="left")
table.add_column("Tipo")
table.add_column("Frete", justify="right")