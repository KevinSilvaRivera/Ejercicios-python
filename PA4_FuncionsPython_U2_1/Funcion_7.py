#CALCULAR EL NUMERO DE DIAGONALES QUE SE PUEDEN TRAZAR A UN POLIGONO DESDE UN SOLO VERTICE

def diagonales(lados):
    canDiag=lados-3
    return canDiag

lados=int(input("Ingrese la cantidad de lados que tiene el poligono "))

print("La cantidad de diagonales que se pueden trazar desde un solo vertice es:",str(diagonales(lados)))