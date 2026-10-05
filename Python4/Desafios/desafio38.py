
class Produto():
    def __init__(self, nome:str, preco:float):
        self._nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self._nome} ({formata_dinheiro(self.preco)})"

class Carrinho():
    def __init__(self, produtos:list = None):
        self.produtos = produtos if produtos else []

    @property
    def total(self):
        return sum(p.preco for p in self.produtos)

    def __add__(self, outro):
        if isinstance(outro, Produto):
            return Carrinho(self.produtos + [outro])
        elif isinstance(outro, Carrinho):
            return Carrinho(self.produtos + outro.produtos)
        else:
            raise TypeError("Você tentou adicionar algo inválido ao carrinho")

    def __str__(self):
        linha = "\n" + "-" * 30
        itens = '\n'.join(str(p) for p in self.produtos)
        return f"{itens}{linha}\nTotal: {formata_dinheiro(self.total)}"


def formata_dinheiro(valor:float):
    import locale
    locale.setlocale(locale.LC_ALL, locale="pt_BR.UTF-8")
    return locale.currency(valor, grouping=True)


p1 = Produto("Notebook", 8_500)
p2 = Produto("Mouse", 250)
p3 = Produto("Fone de Ouvido", 450.35)

c1 = Carrinho()
c2 = Carrinho

c1 = c1 + p1
c1 = c1 + p2
c1 = c1 + p3
print(c1)