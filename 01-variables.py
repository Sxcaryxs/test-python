
#Un simple print
print("Hola soy Diego")

#01-DECLARANDO VARIABLES DE TIPO CADENA DE TEXTO
nombre = "Abel makkonen tesfaye"
name = "Austin post"

#02-IMPRESION DE UNA VARIABLE
print(name)
print("Hola soy",name)

#Declarando una tercera variable de tipo númerico
edad = 29

#03-IMPRESION DE TEXTO + VARIABLE (IMPRESIÓN VARIABLE EDAD)
print("Mi edad es de", edad)

#04-IMPRIMIENDO 2 VARIABLES EN UNA MISMA LINEA 

print('Hola mi nombre es',nombre,"y tengo",edad) #Impresion separando con comas
print("Hola mi nombre es"+" "+name+" "+"y tengo"+str(edad)) #Concatenación con signo +
print(f"Hola mi nombre es {nombre} y tengo {edad} años") #Formato de cadenas literales (f-string)

##05-ACTUALIZANDO LA VARIABLE NOMBRE (Mutabilidad)
nombre = "Duki"
name = "William"
print ("Hola mi nuevo nombre es", nombre)
print ("Hola mi nuevo nombre es", name)

#06-¿VARIABLES EN UNA SOLA LINEA? (No es muy recomendable, solo en ciertas situaciones)
ciudad, region, pais, year = "Puerto Montt", "Los Lagos", "Chile", 2010.
print("Yo naci en la ciudad de", ciudad,", region de",region,pais,", el año",int(year))

#07-UTILIZANDO LA INSTRUCCIÓN INPUT
nombre1 = input("¿Cuál es tu nombre?\n")
edad1 = input("¿Cual es tu edad?\n")

print("Tu nombre es:",nombre1,"y tu edad es", edad1)

#08-ACOTACIÓN CONSTANTES

PI = 3.14
CIUDAD = "Osorno"
