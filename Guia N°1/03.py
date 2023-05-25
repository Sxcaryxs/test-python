Diurno=12000
Nocturno=16000
DiurnoDom=14000
NocturnoDom=19000



trabajador1 = {
    "Jornadas_TrabajadasNoc":3,
    "Jornadas_TrabajadasDiu":2,
    "Turnos_Nocturnos":["Lunes","Martes","Miercoles"],
    "Turnos_Diurnos":["Jueves","Viernes"],
    "Jornadas_NocturnasValor":Nocturno,
    "Jornadas_DiurnasValor":Diurno


}
trabajador2 = {
    "Jornadas_TrabajadasNoc":3,
    "Jornadas_especialesDiu":1,
    "Turnos_Nocturnos":["Martes","Miercoles","Jueves"],
    "Jornadas_NocturnasValor":Nocturno,
    "Jornadas_EspecialesnDiuValor":DiurnoDom


}
trabajador3 = {
    "Jornadas_TrabajadasDiu":3,
    "Jornadas_TrabajadasNoc":1,
    "Jornadas_especialesNoc":1,
    "Turnos_Diurnos":["Miercoles","Jueves","Viernes"],
    "Turnos_Nocturnos":["Sabado"],
    "Jornadas_NocturnasValor":Nocturno,
    "Jornadas_DiurnasValor":Diurno


}
Diu1=Diurno*10*trabajador1.get("Jornadas_TrabajadasDiu")
Noc1=Nocturno*10*trabajador1.get("Jornadas_TrabajadasNoc")
Total1=Diu1+Noc1
trabajador1.setdefault("Total_Semanal")
trabajador1["Total_Semanal"]=Total1
print("Trabajador 1",trabajador1,)
Noc2=Nocturno*10*trabajador2.get("Jornadas_TrabajadasNoc")
espediu2=DiurnoDom*10*trabajador2.get("Jornadas_especialesDiu")
total2=Noc2*espediu2
trabajador2.setdefault("Total_Semanal")
trabajador2["Total_Semanal"]=total2
print(trabajador2)
Diu3=Diurno*10*trabajador3.get("Jornadas_TrabajadasDiu")
Noc3=Nocturno*10*trabajador3.get("Jornadas_TrabajadasNoc")
espenoc3=Nocturno*trabajador3.get("Jornadas_especialesNoc")
Total3=Diu3+Noc3+espenoc3
trabajador3.setdefault("Total_Semanal")
trabajador3["Total_Semanal"]=Total3
print(trabajador3)