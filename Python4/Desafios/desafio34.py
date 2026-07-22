from abc import ABC, abstractmethod

class Funcionario(ABC):
    
    def __init__(self, nome:str = None, salario:float = 1_621):
        self.nome = nome
        self.__salario = salario
    
    @abstractmethod    
    def calcular_bonus():
        pass

    def __str__(self):
        return f"{self.nome} ganha R${self.salario:,.2f} e por ser {self.__class__.__name__} o bônus sera de R${self.calcular_bonus():,.2f}"

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, valor):
        if valor is None:
            raise ValueError("Impossível reajustar o salário desse jeito!")
        else: 
            if valor < self.salario:
                raise ValueError("Você não pode reduzir o salário de um funcionário.")
            else:
                self.__salario = valor


class Gerente(Funcionario): #15%
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def calcular_bonus(self):
        return self.salario * 0.15

class Designer(Funcionario): #8%
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def calcular_bonus(self):
        return self.salario * 0.08

class Desenvolvedor(Funcionario): #10%
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def calcular_bonus(self):
        return self.salario * 0.1


f = Gerente("Pedro", 1_800)
f.salario = 1_500
print(f)