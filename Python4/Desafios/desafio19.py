class Livro():
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
    
    def avancar_paginas(self, quant=1):
        while True:
            for i in range(quant):
                print(f"Pág{quant} ▶")



l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(5)