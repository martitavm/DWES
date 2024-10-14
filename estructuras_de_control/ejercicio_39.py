frase = input("Escribe una frase: ")
contador: int = 0
for letra in frase:
    if(letra == "a" or letra == "e" or letra == "o" or letra == "u"):
        contador+=1

print(contador)