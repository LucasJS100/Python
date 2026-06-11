palavra = "python"
letras = list(palavra)

for i in letras:
    valor_ascii = ord(i)
    repbin = bin(valor_ascii)[2:]
    print(f"{repbin}")