def atringulo(base,altura):
    area=(base*altura)/2
    return area

base=float(input("Ingresa la base"))
altura=float(input("Ingresa la altura"))

area=atringulo(base,altura)
print("El resultado es: ",str(area))