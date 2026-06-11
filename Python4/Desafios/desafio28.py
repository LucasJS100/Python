from rich import inspect

class Termostato():
    def __init__(self, temperatura=24):
        self.__temperatura = temperatura
    
    @property
    def temperatura(self):
        return self.__temperatura
    
    @property
    def ftemperatura(self):
        return f"{self.__temperatura}ºC"
    
    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 == 0:
            if 16 <= valor <= 30:
                self.__temperatura = valor  
            elif valor > 30:
                self.__temperatura = 30
            elif valor < 16:
                self.__temperatura = 16
        else:
            print("Valor Inválido, escolha números multiplos de 0.5")

t = Termostato()
t.temperatura = 25.2
inspect(t, private=True, methods=True)
print(f"A temperatura atual é {t.ftemperatura}")