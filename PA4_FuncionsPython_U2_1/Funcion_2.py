#CALCULAR EL PERIMETRO Y AREA DE UN RECTANGULO

def perimetroR(b,h):
    peri=2*(b+h)
    return peri

def areaR(b,h):
    area=b*h
    return area

b=float(input("Ingrese el valor de la base "))
h=float(input("Ingrese el valor de la altura "))

print("El perimetro del rectangulo es", str(perimetroR(b,h)))
print("Al area de el rectangulo es:", str(areaR(b,h)),"U²")