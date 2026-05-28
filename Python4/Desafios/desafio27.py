from abc import ABC,abstractmethod
from random import randint, choice
from rich import print
from time import sleep

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []
    
    def atacar(self, alvo, forca):
        dano = randint(1, forca)
        print(f"[bold green]{self.nome}[/bold green]([bold cyan]{self.vida}[/bold cyan]) atacou [bold red]{alvo.nome}[/bold red]([bold cyan]{alvo.vida}[/bold cyan]) com um [bold blue]{choice(self.golpes)}[/bold blue] de força [bold cyan]{forca}[/bold cyan]")

        vida_antes = alvo.vida
        alvo.receber_dano(dano)

        print(f"[bold blue]{alvo.nome}[/bold blue] recebeu [red]dano de [bold]{dano}[/bold][/red]!")
        
        if alvo.vida <= 0:
            if (dano / vida_antes) > 2:
                print(f"[bold red]OVERKILL![/bold red] [bold blue]{self.nome}[/bold blue] esmagou {alvo.nome} com dano de {dano}.")
            else:
                print(f"[bold blue]{self.nome}[/bold blue] derrotou {alvo.nome} com um [bold red]golpe fatal[/bold red]!")
        else:
            print(f"[bold blue]{alvo.nome}[/bold blue] permanece [bold green]vivo[/bold green]!")

    def receber_dano(self, dano):
        self.vida -= dano

        if self.vida < 0:
            self.vida = 0

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Chute Giratorio", "Corte Horizontal", "Arrancada", "Golpe de Machado"]
    
    def curar(self):
        cura = randint(1, 100)
        self.vida += cura
        print(f"[bold blue]{self.nome}[/bold blue] usou uma poção de cura e [green]recuperou [bold]{cura}[/bold] pontos[/green] de vida.")
        print(f"A [bold green]vida atual[/bold green] de [bold blue]{self.nome}[/bold blue] é [bold green]{self.vida}[/bold green]!")

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de fogo", "Raio Congelante", "Trovoada", "Cuspe Acido", "Tufão", "Prisão de Agua"]

    def curar(self):
        cura = randint(1, 100)
        self.vida += cura
        print(f"[bold blue]{self.nome}[/bold blue] fez uma magia de cura e [green]recuperou [bold]{cura}[/bold] pontos[/green] de vida.")
        print(f"A [bold green]vida atual[/bold green] de [bold blue]{self.nome}[/bold blue] é [bold green]{self.vida}[/bold green]!")



nomesAleatorioGuerreiro = ["Guts", "Zoro", "Dante", "Musashi Miyamoto", "He-man", "Sun Wukong", "Artorias", "Askeladd"]
nomesAleatorioMago = ["Ainz", "Anos", "Julius Novachrono", "Frieren", "Sung", "Aladdin", "Yuno", "Shirou"]

# BOT
aleatorio = randint(1, 2)

match aleatorio:
    case 1:
        p2 = Guerreiro(choice(nomesAleatorioGuerreiro), randint(3000, 5000))
    case 2:
        p2 = Mago(choice(nomesAleatorioMago), randint(1000, 2000))

try:
    while True:

        # Criação do Personagem
        escolha = str(input("Escolha uma classe entre guerreiro e mago: ")).strip().lower()
        if escolha == "mago":
            nome = str(input("Escolha seu nome de mago: "))
            vida = int(input("Escolha a quantidade de vida(Max:2000): "))
            p1 = Mago(nome, vida)
            break
        elif escolha == "guerreiro":
            nome = str(input("Escolha seu nome de guerreiro: "))
            vida = int(input("Escolha a quantidade de vida(Max:5000): "))
            p1 = Guerreiro(nome, vida)
            break
        else:
            print("Escolha uma classe existente.")


    while p1.vida > 0 and p2.vida > 0:
        # Escolha de ações
        print('-'*30)
        print(f"[green]Sua vida: [bold]{p1.vida}[/bold][/green] | [red]Vida de {p2.nome}: {p2.vida}[/red]")
        print("Escolha uma ação contra o player 2")
        print("1. Atacar")
        print("2. Curar")
        print("3. Sair")
        try:
            acao = int(input("Escolha: "))
        except ValueError:
            print("Por favor, digite um número.")
            continue


        jogou = False
        match acao:
            case 1:
                forca = int(input("Escolha o tanto de força de ataque(Max:2500)"))
                p1.atacar(p2, forca)
                jogou = True
            case 2:
                p1.curar()
                jogou = True
            case 3:
                print("Saindo do jogo")
                sleep(0.7)
                print("\n.")
                sleep(0.7)
                print("\n.")
                sleep(0.7)
                print("\n.")
                sleep(0.7)
                break
            case _:
                print("Opção inválida")
        if jogou and p2.vida > 0:
            print(f"\n[yellow] Turno de {p2.nome}...[/yellow]")

            acao_bot = randint(1, 2)
            if acao_bot == 1:
                p2.atacar(p1, randint(1000, 2500))
            else:
                p2.curar()
        
    print("\n[bold yellow]=== FIM DA BATALHA ===[/bold yellow]")
    if p1.vida <= 0:
        print(f"[bold red]Você foi derrotado por {p2.nome}![/bold red]")
    elif p2.vida <= 0:
        print(f"[bold green]Para´bens! Você derrotou {p2.nome}![/bold green]")
except KeyboardInterrupt:
    pass