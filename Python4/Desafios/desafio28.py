from rich import inspect

class Termostato():
    def __init__(self):
        self.__temperatura = 24
    
    @property
    def temperatura(self):
        return self.__temperatura
    
    @property
    def ftemperatura(self):
        return f"{self.__temperatura}{chr(176)}C"
    
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
            raise ValueError(f"Temperatura de {valor}{chr(176)}C é inválida!")

t = Termostato()
t.temperatura = 25
inspect(t, private=True, methods=True)
print(f"A temperatura atual é {t.ftemperatura}")