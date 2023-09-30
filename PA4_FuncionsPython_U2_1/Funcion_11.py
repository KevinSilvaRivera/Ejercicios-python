#CALCULAR LA ENERGIA POTENCIAL DE UNA PARTICULA

def energiaPo(masa,altura):
    energiaPotencial=masa*9.81*altura
    energiaPotencial="{:.4f}".format(energiaPotencial)
    return energiaPotencial

masa=float(input("Ingrese la masa de la particula(kg) "))
altura=float(input("Ingrese la altura a la que se encuentra la particula(m) "))

print("La energia potencial de la particula es de:",str(energiaPo(masa,altura)),"J")