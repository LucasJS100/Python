from rich import print
from rich.panel import Panel

class Churrasco():
    def __init__(self, titulo="", quant=0):
        self.titulo = titulo
        self.quant = quant
    
    def analisar(self):
        recomendado = self.quant * 0.4
        carnetotal = recomendado * 82.40
        carnePP = carnetotal / self.quant

        print(Panel(f"Analisando [green]{self.titulo}[/green] com [blue]{self.quant} convidados[/blue]\n Cada participante comerá 0.4Kg e cada Kg custa R$82.40\n Recomendo [blue]comprar {recomendado}Kg[/blue] de carne \n O custo total será de [blue]R${carnetotal:.2f}[/blue]\n Cada pessoa pagará [yellow]R${carnePP:.2f}[/yellow] para participar."))

c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()