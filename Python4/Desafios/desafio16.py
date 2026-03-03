class Funcionario():
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def aprensentar(self):
        print(f"🤝 Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa Curso Em Vídeo")


c1 = Funcionario("Maria", "Admnistração", "Diretoria")
print(c1.aprensentar())

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.aprensentar())