from rich import print, inspect

class Retangulo():
    def __init__(self, base=0, altura=0):
        self._base = base
        self._altura =  altura
        self._area = None
    
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, base):
        if base > 0:
            self._base = base
        else:
            raise ValueError("Valor inválido para a base")
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, altura):
        if altura > 0:
            self._base = altura
        else:
            raise ValueError("Valor inválido para a altura")

    @property
    def area(self):
        return self._base * self._altura
    
    @property
    def medidas(self):
        return f"Base = {self._base} \nAltura = {self._altura} \nÁrea = {self.area}"
    
    @medidas.setter
    def medidas(self, valores):
        base, altura = valores
        self._base = base
        self._altura = altura

r = Retangulo()

r.base = -12
r.altura=33

#r.medidas = (9, 3)
#print(r.medidas)

#inspect(r, private=True, methods=True)