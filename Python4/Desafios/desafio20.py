from rich import print
from rich.panel import Panel

class Gamer():
    listaFav = []

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
    
    def add_favoritos(jogo):
        listaFav.append(jogo)

    def ficha(self):
        for i in range(len(listaFav))
        print(Panel(f"Nome real: {self.nome}\nJogos favoritos: "))