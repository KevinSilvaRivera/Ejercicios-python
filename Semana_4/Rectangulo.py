def perimetroR(b,h):
    peri=2*(b+h)
    print("El perimetro del rectangulo es ",str(peri))


def areaR(b,h):
    area=b*h
    print("Al area de el rectangulo es: ", str(area))

b=float(input("Ingrese el valor de la base "))
h=float(input("Ingrese el valor de la altura "))

perimetroR(b,h)
areaR(b,h)

