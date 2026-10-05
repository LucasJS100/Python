from abc import ABC, abstractmethod
import locale

class Pagamento(ABC):
    def __init__(self):
        self._valor = None

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, valor:float):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError(f"O pagamento só pode ser efetuado para valores positivos.")
    
    @property
    def fvalor(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return  locale.currency(self._valor, grouping=True)

    @abstractmethod
    def pagar(self, valor:float):
        pass

class Boleto(Pagamento):
    def pagar(self, valor):
        try:
            self.valor = valor
            return f"Pagamento CONFIRMADO de {self.fvalor} via Boleto"
        except:
            return f"Falha no pagamento de {self.fvalor} via Boleto"


class Pix(Pagamento):
    def pagar(self, valor):
        try:
            self.valor = valor
            return f"Pagamento CONFIRMADO de {self.fvalor} via PIX"
        except:
            return f"Falha no pagamento de {self.fvalor} via PIX"


class CartaoCrédito(Pagamento):
    def pagar(self, valor):
        try:
            self.valor = valor
            return f"Pagamento CONFIRMADO de {self.fvalor} via Cartão de Crédito"
        except:
            return f"Falha no pagamento de {self.fvalor} via Cartão de Crédito"


def finalizar_compra(forma:Pagamento, valor:float):
    print(forma.pagar(valor))


finalizar_compra(CartaoCrédito(), 25_324.20)