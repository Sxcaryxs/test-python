a=float(input("Primer lado "))
b=float(input("Segundo lado "))
c=float(input("Tercer lado "))



if a==b==c:
    print("Equilatero")
    if a!=b!=c:
        print("Escaleno")
else:
    print("Isoceles")

p=(a+b+c)/2
Area=(p*(p-a)*(p-b)*(p-c))**(1/2)

print("Segun la forma de heron el area del triangulo es ",Area)