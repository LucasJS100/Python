from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados
    
    @abstractmethod
    def perimetro(self):
        pass
    
    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, qtd_lados):
        super().__init__(qtd_lados)
    
    def perimetro(self):
        return self.qtd_lados + self.qtd_lados + self.qtd_lados + self.qtd_lados
    
    def area(self):
        return self.qtd_lados ** 2

class Circulo(Poligono):
    def __init__(self, qtd_lados=0):
        super().__init__(qtd_lados)
    
    def perimetro(self):
        return (self.qtd_lados * 2) * pi
    
    def area(self):
        return pi * self.qtd_lados**2

p1 = Circulo(20)
print(f"Perímetro = {p1.perimetro():.1f}")
print(f"Area = {p1.area():.1f}")