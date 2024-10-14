num = int(input("Ingresa tu nota: "))

if 0 <= num <= 4 :
    print("Suspenso")
elif 5 >= num <= 6:
    print("Aprobado")
elif 7 >= num <= 8:
    print("Notable")
else:
    print("Sobresaliente")