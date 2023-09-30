#PROGRAMA QUE CALCULA EL PROMEDIO DE UN ESTUDIANTE QUE CURSA LAS SIGUIENTES MATERIAS: METROLOGIA, ALGEBRA, CALCULO, ECONOMIA, ESTADISTICA, ESTUDIO DEL TRABAJO.

print("PROGRAMA QUE CALCULA EL PROMEDIO DE UN ESTUDIANTE\n\nIngrese las calificaciones en el siguiente orden:")
mtr=float(input("Metrologia: "))
mtr=mtr+float(input("Algebras: "))
mtr=mtr+float(input("Calculo: "))
mtr=mtr+float(input("Economia: "))
mtr=mtr+float(input("Estadistca: "))
mtr=mtr+float(input("Estudio del trabajo: "))

print("Promedio: "+str(mtr/6))
