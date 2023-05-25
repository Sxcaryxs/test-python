n = int(input("Dame el numero del cubo: "))

suma = 0

for i in range(1, n + 1 ):
    suma += i*2 - 1
    cubo = suma**3
    print(f"El cubo {i} es: {cubo}")
