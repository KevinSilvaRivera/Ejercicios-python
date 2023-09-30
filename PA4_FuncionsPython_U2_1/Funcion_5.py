#CALCULAR EL PERIMETRO Y AREA DE UN HEXAGONO.

from math import sqrt

def perimetroH(lado):
    peri=lado*6
    return peri

def areaH(lado):   
    area=6*(((lado**2)*(sqrt(3)))/4)
    area="{:.4f}".format(area)
    return area
    
lado=float(input("Ingrese el valor de uno de sus lados "))

print("El perimetro del hexagono es:",str(perimetroH(lado)))
print("El area del hexagono es:",str(areaH(lado)),"U²")