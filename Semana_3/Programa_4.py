
suma=0
for i in range(6):
    
    cal =float(input("Ingrese la calificacion "))
    suma= suma+cal
    
promedio = suma/6

if promedio >= 70:
    print("Aprobado con ", str(promedio))

else: 
    print("Reprobado con ", str(promedio))

