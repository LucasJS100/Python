from rich import print, inspect

class Retangulo():
    def __init__(self, base=1, altura=1):
        self._base = None
        self._altura =  None
        self._area = None
        self.base = base
        self.altura  = altura
    
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, base):
        if not isinstance(base, float) and not  isinstance(base, int):
            raise TypeError("O valor da base deve ser um número.")
        elif base < 0:
            raise ValueError("Valor inválido para a base")
        else:
            self._base = base
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, altura):
        if altura > 0:
            self._altura = altura
        else:
            raise ValueError("Valor inválido para a altura")

    @property
    def area(self):
        return self._base * self._altura
    
    @area.setter
    def area(self):
        raise PermissionError("Área não pode ser configurada desse jeito.")
    
    @property
    def medidas(self):
        return f"Base = {self._base} \nAltura = {self._altura} \nÁrea = {self.area}"
    
    @medidas.setter
    def medidas(self, valores):
        base, altura = valores
        self._base = base
        self._altura = altura

r = Retangulo()
r.base = 4
r.altura = 9

print(r.medidas)


#r.medidas = (9, 3)
#print(r.medidas)

#inspect(r, private=True, methods=True)