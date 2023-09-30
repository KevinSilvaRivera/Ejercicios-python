#CALCULAR LA SUMA DE LOS ANGULOS INTERIORES DE UN POLIGONO REGULAR

def sumaAng(lados):
    suma=(lados-2)*180
    return suma

lados=int(input("Ingresa la cantidad de lados del poligono "))

print("La suma de la los angulos interiores del poligono es:",str(sumaAng(lados)),end="°")