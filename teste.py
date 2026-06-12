palavra = "python"
valor_bits = len(palavra) * 8
valor_juntar = 448 - (valor_bits + 1) 
letras = list(palavra)
zero = '0'
valor_bin = ""

for i in letras:
    valor_ascii = ord(i)
    repbin = bin(valor_ascii)[2:].rjust(8, '0')
    valor_bin += repbin

valor_bin += '1'

print(valor_juntar)

for i in range(1, valor_juntar + 1):
    valor_bin += '0'
valor_bin += bin(valor_bits)[2:].rjust(64, '0')

print(len(valor_bin))
