from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome, ext:str , tamanho):
        self.nome = nome
        self._extensao = None
        self.tamanho = tamanho
        self.extensao = ext

    @abstractmethod
    def abrir(self):
        pass

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, ext:str):
        formatos = ['pdf', 'doc', 'docx']
        ext = ext.lower().strip()
        if ext in formatos:
            self._extensao = ext
        else:
            raise AttributeError("O Arquivo está em um formato não suportado")
    
    @property
    def nome_completo(self):
        return f"'{self.nome}.{self.extensao}'({self.tamanho/1000000}MB)"

class PDF(Arquivo):
    def __init__(self, nome:str, tamanho:int):
        super().__init__(nome, 'pdf', tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader")

class DOC(Arquivo):
    def __init__(self, nome:str, tamanho:int):
        super().__init__(nome, 'docx', tamanho)
    
    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Microsoft Word")

def abrir_arquivo(arq):
    arq.abrir()

a1 = DOC("prova", 250_000)
a2 = PDF("contrator", 1_300_000)

abrir_arquivo(a1)
abrir_arquivo(a2)