nom1=input("Nombre ")
while nom1!=str:
    print("Debe ingresar un nombre ")
    nom1=input("Nombre ")
nom2=input("Nombre de otra persona ")
while nom2!=str:
    print("Debe ingresar un nombre ")
    nom2=input("Nombre de otra persona ")


nombre1=list(nom1)
nombre2=list(nom2)

if nombre1[0]==nombre2[0]:
    print("La primera letra de los nombres coinciden")

if nombre1[-1]==nombre2[-1]:
    print("la ultima letra de los nombres coinciden")

else:
    print("Ningun nombre coincide")
    

