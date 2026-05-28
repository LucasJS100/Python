from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    def __init__(self, nome, sal_bruto=0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.sal_min = 1612
        self.inss = 7.5
    
    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        calc = self.calc_sal()
        texto = f"O salário de [bold blue]{self.nome}[/bold blue] ([bold purple]{self.__class__.__name__}[/bold purple]) é de [bold green]R${self.calc_sal()}[/bold green] e corresponde a [bold yellow]{calc / self.sal_min:.1f} salários mínimos[/bold yellow]."

        print(Panel(texto, title="Análise de Salário", width=48))


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome, sal_bruto=0)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        salario = self.valor_hora * self.horas_trab
        porcent = self.inss / 100
        return salario - (salario * porcent)
    
class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto)
    
    def calc_sal(self):
        porcent = self.inss / 100
        return self.sal_bruto - (self.sal_bruto * porcent)

f1 = FuncionarioHorista("Paulo", 12, 200)
f1.calc_sal()
f1.analisar_sal()

f2 = FuncionarioMensalista("Amanda", 9500)
f2.calc_sal()
f2.analisar_sal()