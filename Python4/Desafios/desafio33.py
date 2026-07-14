from abc import ABC
from rich import print, inspect
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome:str , nasc:int):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nasc
    
    @property
    def nascimento(self):
        return self._nascimento
    
    @nascimento.setter
    def nascimento(self, ano:int):
        ano_atual = date.today().year
        if 1900 <= ano <= ano_atual:
            self._nascimento = ano
        else:
            raise ValueError(f"Ano {self._nascimento} é invalido")

    @property
    def idade(self):
        ano_atual = date.today().year
        return ano_atual - self._nascimento
    
    @idade.setter
    def idade(self, valor):
        raise PermissionError("Você não pode alterar a idade. Mude o ano de nascimento")
    


class Aluno(Pessoa):

    cursos_oficiais = ['ADM', "ADS", "ENG", "CONT"]


    def __init__(self, nome:str, nasc:int , curso:str):
        super().__init__(nome, nasc)
        self._curso = None
        self.curso = curso
    
    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, curso):
        if curso in Aluno.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f"O Curso {curso} não está na lista de cursos oficiais.")
    
    def add_curso(self, curso:str):
        curso = curso.strip().upper()
        if 3 <= len(curso) <= 5:
            if curso in Aluno.cursos_oficiais:
                raise ValueError(f"Curso de {curso} já está na lista.")
            else:
                Aluno.cursos_oficiais.append(curso)
        else:
            raise ValueError(f"Nome {curso} está fora do padrão para Cursos!")
    

a = Aluno("Marcia", 2010, "ADM")
b = Aluno("Pedro", 2015, "ENG")

a.add_curso("ADS")

print(b.cursos_oficiais)
print(a.__dict__)