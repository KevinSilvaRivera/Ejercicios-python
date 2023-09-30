#CALCULAR EL PERIMETRO Y AREA DE UN CIRCULO.
#Kevin Silva Rivera

from math import pi

def perimetroCirculo(radio):
    perimetro=(2*pi)*radio
    perimetro="{:.4f}".format(perimetro)
    return perimetro

def areaCirculo(radio):
    area=pi*(radio**2)
    area="{:.4f}".format(area)
    return area

radioCirculo=float(input("Ingrese el valor del radio del circulo "))

print("El perimetro del circulo es:",str(perimetroCirculo(radioCirculo)))
print("El area del circulo es:",str(areaCirculo(radioCirculo)),"U²")