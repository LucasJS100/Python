from rich import inspect, print
from rich.panel import Panel

class Mensagem():
    def __init__(self, mensagem:str = '', tipo:str = 'Aviso', icone:str = ':speech_balloon:'):
        self._mensagem = mensagem
        self._tipo = tipo
        self._icone = icone

    def mostrar(self):
        msg = Panel(self._mensagem, title=f"{self._icone} {self._tipo.upper()} {self._icone}", width=50, style="#ffffff on #000000")
        print(msg)

class Erro(Mensagem):
    def __init__(self, mensagem = '', tipo = 'erro', icone = ':no_entry_sign:'):
        super().__init__(mensagem, tipo, icone)
    def mostrar(self):
        msg = Panel(self._mensagem, title=f"{self._icone} {self._tipo.upper()} {self._icone}", width=50, style="#ffff00 on #880000")
        print(msg)


class Alerta(Mensagem):
    def __init__(self, mensagem = '', tipo = 'alerta', icone = ':warning:'):
        super().__init__(mensagem, tipo, icone)
    def mostrar(self):
        msg = Panel(self._mensagem, title=f"{self._icone} {self._tipo.upper()} {self._icone}", width=50, style="#000000 on #fffc1b")
        print(msg)



Erro("Olá, Gafanhoto!").mostrar()