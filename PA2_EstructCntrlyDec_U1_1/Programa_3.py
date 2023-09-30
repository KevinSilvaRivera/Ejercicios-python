#PROGRAMA QUE CALCULA EL IMC (INDICE DE MASA CORPORAL) DE UNA PERSONA

print("PROGRAMA QUE CALCULA EL IMC (INDICE DE MASA CORPORAL) DE UNA PERSONA\n")
peso=float(input("Ingrese el peso en kilogramos(kg): "))
altura=float(input("Ingrese la altura en metros(m): "))

imc=peso/pow(altura,2)

print("Su IMC es de: "+str(imc)+" kg/m²")

