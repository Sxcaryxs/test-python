import random

contador=20
numeros=[]

while contador>=0:
    numeros.append(random.randrange(40,350))
    contador=contador-1
print(numeros)
Numero=int(input("Eliga un numero entre 40 y 350 que quiera buscar: "))
if Numero not in numeros:
    print("El numero no esta en la lista")
else:
    print("El numero Esta en la lista")
    print("El numero se repite",numeros.count(Numero),"Veces")