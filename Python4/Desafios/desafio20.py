from rich import print
from rich.panel import Panel

class Gamer():

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.listaFav = []
    

    def add_favoritos(self, jogo):
        self.listaFav.append(jogo)
        self.listaFav.sort()

    def ficha(self):
        conteudo = f"Nome real: {self.nome}\n"
        conteudo += f"Jogos favoritos: "

        for j in self.listaFav:
            conteudo += f"\n:video_game: [blue]{j}[/]"
        
        print(Panel(conteudo, title=f'Jogador <{self.nick}>', width=50))

j1 = Gamer("Fabricio da Silva", "detonator2025")
j1.add_favoritos("Mario Bros.")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()

j2 = Gamer("Olívia Souza", "peach_raivosa")
j2.add_favoritos("Mario Bros")
j2.add_favoritos("Call of Duty")
j2.ficha()