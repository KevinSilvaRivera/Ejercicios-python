def perimetro(lado, apotema):
    peri=lado*6
    apo=apotema
    areaH(peri,apo)
    print("El perimetro es: ",str(peri))

def areaH(peri,apo):   
    area=(peri*apo)/2
    print("El area del hexagono es: ",str(area)," U²")
    
lado=float(input("Ingrese el valor de uno de sus lados "))
apotema=float(input("Ingrese el valor de la apotema "))

perimetro(lado, apotema)