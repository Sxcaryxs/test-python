print("Ingrese los datos del  primer paciente")
nombre1=str(input("Ingrese el nombre "))
edad1=int(input("Ingrese la edad "))
while edad1>150 and edad1<=0:
    edad1=int(input("Ingrese una edad valida "))
peso1=int(input("Ingrese el peso "))
estatura1=float(input("Ingrese la estatura "))



print("Ingrese los datos del  segundo paciente")
nombre2=str(input("Ingrese el nombre "))
edad2=int(input("Ingrese la edad "))
while edad2>150 and edad2<=0:
    edad2=input("Ingrese una edad valida ")
peso2=int(input("Ingrese el peso "))

estatura2=float(input("Ingrese la estatura "))



print("Ingrese los datos del  tercer paciente")
nombre3=str(input("Ingrese el nombre "))
edad3=int(input("Ingrese la edad "))
while edad3>150 and edad3<=0:
    edad3=input("Ingrese una edad valida ")
peso3=int(input("Ingrese el peso "))
estatura3=float(input("Ingrese la estatura "))

datos1=(nombre1,peso1,estatura1,edad1)
datos2=(nombre2,peso2,estatura2,edad2)
datos3=(nombre3,peso3,estatura3,edad3)

Datospacientes=[datos1,datos2,datos3]