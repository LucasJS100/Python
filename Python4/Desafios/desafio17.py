from rich import print
from rich.panel import Panel

class Produto():
    def __init__(self, nome='vazio', preco=0):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        preco_br = f"R$ {self.preco:,.2f}"

        conteudo = (f"{self.nome.center(15, ' ')}")
        conteudo += f"{'-'*30}"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(15, '.')}"

        print(Panel(conteudo, title="Produto", style="white", width=34))

p1 = Produto("Iphone 17 Pro Max", 25_000.85)
p2 = Produto("Notebook Gamer", 8_000)

p1.etiqueta()
p2.etiqueta()