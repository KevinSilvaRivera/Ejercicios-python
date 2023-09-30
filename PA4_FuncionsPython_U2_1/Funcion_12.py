#CALCULAR EL PUNTO MEDIO DE UN SEGMENTO DE RECTA DADOS DOS PUNTOS

def puntoMedio(x1,y1,x2,y2):
    x3=int((x1+x2)/2)
    y3=int((y1+y2)/2)
    return x3,y3

x1=int(input("Ingrese la cordana x del primer punto: "))
y1=int(input("Ingrese la cordana y del primer punto: "))
x2=int(input("Ingrese la cordana x del segundo punto: "))
y2=int(input("Ingrese la cordana y del segundo punto: "))

print("El punto medio es:",str(puntoMedio(x1,y1,x2,y2)))