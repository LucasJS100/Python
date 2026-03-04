from rich import print
from rich.panel import Panel

class Churrasco():
    def __init__(self, titulo="", quant=0):
        self.titulo = titulo
        self.quant = quant
    
    def recomendado(self):
        return self.quant * 0.4
    
    def carneTotal(self):
        return self.recomendado() * 82.40

    def carnePP(self):
        return self.carneTotal() / self.quant

    def analisar(self):

        conteudo = f"Analisando [green]{self.titulo}[/green] com [blue]{self.quant} convidados[/blue] "
        conteudo += f"Cada participante comerá 0.4Kg e cada Kg custa R$82.40 "
        conteudo += f"Recomendo [blue]comprar {self.recomendado()}Kg[/blue] de carne "
        conteudo += f"O custo total será de [blue]R${self.carneTotal():,.2f}[/blue] "
        conteudo += f"Cada pessoa pagará [yellow]R${self.carnePP():.2f}[/yellow] para participar."

        print(Panel(conteudo, title=self.titulo, width=70   ))


c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()