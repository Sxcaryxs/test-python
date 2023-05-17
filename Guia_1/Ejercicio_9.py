numeros=[4,3,8,12,6,10,14,3,6]

numeros.pop(-1)
print("Ultimo numero borrado",numeros)
numeros.insert(0,2)
print("Dos insertado al inicio",numeros)


resultado = []
 
for element in numeros:
    if element not in resultado:
        resultado.append(element)
numeros=resultado

print("Lista sin dos elementos iguales",numeros)

suma=len(numeros)
media=sum(numeros)/len(numeros)
print(suma)
print("La media es",media)




print(numeros)
