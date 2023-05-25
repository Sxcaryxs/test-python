grupo1 = {"Marcos","Gabriela","Benjamin","Matias"}
grupo2 = {"Marcos","Nicolas","Diego","Matias"}

if len(grupo1.intersection(grupo2))>=1:
    print("Hay nombres repetidos los cuales son ",grupo1.intersection(grupo2))
else:
    print("no hay nombres repetidos")
