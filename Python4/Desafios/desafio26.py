from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    sal_min = 1_612
    inss = 7.5

    def __init__(self, nome = None):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0
    
    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        base = self.salario / Funcionario.sal_min

        texto = f"O salário de [bold blue]{self.nome}[/bold blue] ([bold purple]{self.__class__.__name__}[/bold purple]) é de [bold green]R${self.salario}[/bold green] e corresponde a [bold yellow]{base:.1f} salários mínimos[/bold yellow]."

        print(Panel(texto, title="Análise de Salário", width=48))


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora=7.37, horas_trab=220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.sal_bruto = self.valor_hora * self.horas_trab

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100)
    
class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, sal_bruto=Funcionario.sal_min):
        super().__init__(nome)
        self.sal_bruto = sal_bruto
    
    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100)

f1 = FuncionarioHorista("Paulo", 25, 250)
f1.calc_sal()
f1.analisar_sal()

f2 = FuncionarioMensalista("Amanda", 8500)
f2.calc_sal()
f2.analisar_sal()