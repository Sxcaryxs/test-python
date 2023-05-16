w1=(input("Ingrese la primera palabra "))
w2=(input("Ingrese la segunda palabra "))

#Usar len y unos if#

if len(w1)>len(w2):
    print("La palabra",w1,"tiene mas palabras")
    print("La palabra",w2,"Tiene menos palabras")
if len(w2)>(w1):
    print("La palabra",w2,"tiene mas palabras")
    print("La palabra",w1,"Tiene menos palabras")
if len(w1)==len(w2):
    print("Ambos tiene la misma cantidad de palabras")
    


