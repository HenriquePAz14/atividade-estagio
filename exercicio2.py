texto = input("digite um texto: ")
quantidade = 0 
if (texto != ""):
    for i in texto:
        if (i == "a" or i == "A"):
            quantidade += 1
            print(texto)

print("Seu texto tem a letra a escrita", quantidade, "vezes")