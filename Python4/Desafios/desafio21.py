from rich import print

class Caneta():
    def __init__(self, cor='azul'):
        escolha = ''
        match cor.lower().strip():
            case 'azul':
                escolha = "[blue]"
            case 'vermelha' | "vermelho":
                escolha = "[red]"
            case 'verde':
                escolha = '[green]'
            case _:
                escolha = '[white]'
        self.cor = escolha
        self.tampada = True

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def escrever(self, msg):
        if self.tampada:
            print(f":pohibited: A {self.cor} caneta[/] está tampada!")
        else:
            print(f"{self.cor}{msg}[/]", end='')

    def quebrar_linha(self, quant=1):
        ...