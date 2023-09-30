#CALCULAR EL INDICE DE MASA CORPORAL DE UNA PERSONA

def imcFun(peso,altura):
    imc=peso/pow(altura,2)
    imc="{:.4f}".format(imc)
    return imc

peso=float(input("Ingrese el peso en kilogramos(kg): "))
altura=float(input("Ingrese la altura en metros(m): "))

print("El IMC es de:",imcFun(peso,altura))