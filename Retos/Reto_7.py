def Diccionario():
    palabra=input("Ingrese palabra: ")
    dic={palabra,}
    
    
    opcion=input("Agregar otra palabra? Si/No:")
    while opcion=="Si":
        otrapalabra=input("Ingrese palabra: ")
        dic.add(otrapalabra)
        opcion=input("Agregar otra palabra? Si/No:")
    cantidad=len(dic)
    print("El tamaño del diccionario es de ",cantidad)
    print(dic)
Diccionario()