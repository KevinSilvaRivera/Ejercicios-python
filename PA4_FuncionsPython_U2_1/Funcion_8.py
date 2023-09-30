#CALCULAR EL NUMERO DE DIAGONLAES TOTALES QUE SE PUEDEN TRAZAR A UN POLIGONO

def diagonalesTotal(lados):
    canDiag=(lados*(lados-3))/2
    canDiag=int(canDiag)
    return canDiag

lados=int(input("Ingrese la cantidad de lados que tiene el poligono "))

print("La cantidad de diagonales totales que se pueden trazar en el poligono es:",str(diagonalesTotal(lados)))