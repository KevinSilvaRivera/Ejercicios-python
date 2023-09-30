a=float(input("Introduce un numero: "))
b=(input("Introduce otro numero: "))

suma=a+b
resta=a-b
mult=a*b
div=a/b

pot = pow(a,b)

raiz2 = pow(a,1/b)

print("La suma de los dos numeros es:" +str(suma))
print("La resta de los dos numeros es:" +str(resta))
print("La multiplicacion de los dos numeros es:" +str(mult))
print("La division de los dos numeros es:" +str(div))
print("La potencia del numero es:" +str(pot))

print("La raiz del numero es:" +str(raiz2))