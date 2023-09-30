#CALCULAR LA ENERGIA CINETICA DE UNA PARTICULA

def energiaCine(masa,velocidad):
    energia=0.5*(masa*velocidad**2)
    return energia

masa=float(input("Ingrese la masa de la particula(kg) "))
velocidad=float(input("Ingrese la velocidad de la particula(m/s) "))

print("La energia cinetica de la particula es de:",str(energiaCine(masa,velocidad)),"J")