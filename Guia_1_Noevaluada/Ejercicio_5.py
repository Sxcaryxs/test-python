n1=float(input("Primer laboratorio "))
while n1>7 or n1<=0:
    print("ingrese una nota valida ")
    n1=float(input("Primer laboratorio "))

n2=float(input("Segundo laboratorio "))
while n2>7 or n2<=0:
    print("ingrese una nota valida ")
    n2=float(input("Segundo laboratorio "))

n3=float(input("Tercer laboratorio "))
while n3>7 or n3<=0:
    print("ingrese una nota valida ")
    n3=float(input("Segundo laboratorio "))

promedio=n1*0.3 + n2*0.4 + n3*0.3

if promedio<4:
    print("Asignatura reprobada")
if promedio==4:
    print("Asignatura aprobada")

if promedio>=4 and promedio>5:
    print("Asignatura aprobada")
if promedio>=6:
    print("Promedio aprobado con distincion")


