lista1 = [10,20 ,30, 40, 50 ]
lista2 = [18,22,65, 37, 45]
lista_multiplicada = []

for num1, num2 in zip(lista1, lista2):
    lista_multiplicada.append(num1 * num2)

print(lista_multiplicada)