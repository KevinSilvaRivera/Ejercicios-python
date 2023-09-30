#Funcion que calcula el area de un cuadrado

def areaCuadrado(lado):
    area=lado*lado
    return area

lado=float(input("Ingrese el tamaño de uno de sus lados "))
print("El area del cuadrado es:",str(areaCuadrado(lado)),"U²")