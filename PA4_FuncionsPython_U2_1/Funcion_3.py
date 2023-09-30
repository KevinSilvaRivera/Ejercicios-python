#CALCULAR EL AREA DE UN TRIANGULO

def atringulo(base,altura):
    area=(base*altura)/2
    return area

base=float(input("Ingresa la base "))
altura=float(input("Ingresa la altura "))

print("El area del triangulo es:",str(atringulo(base,altura)),"U²")