print("Cuantas veces se repite la palabra univercidad")
Palabra = "universidad"
PalabraM= "Universidad"
lista=[]
texto = "La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad suspilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacipacion democratica."
toctal=texto.count(Palabra)+texto.count(PalabraM)
print("La palabra " + Palabra + " se repite " + str(toctal) + " veces")
numeromin=texto.count(Palabra)
numeromay=texto.count(PalabraM)
while numeromin>0:
    lista.append(Palabra)
    numeromin=numeromin-1
while numeromay>0:
    lista.append(PalabraM)
    numeromay=numeromay-1

tupla=(lista)
print(tupla)
