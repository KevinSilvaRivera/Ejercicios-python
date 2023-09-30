#PROGRAMA QUE IMPRIME LOS NUMEROS DEL 1 AL 50 E IMPRIME LA SUMA DE ELLOS.

print("PROGRAMA QUE IMPRIME LOS NUMEROS DEL 1 AL 50 E IMPRIME LA SUMA DE ELLOS\n")
suma = 0
for i in range(1,51):
    suma = suma+i
    if i < 50:
        print(i, end=", ")
    else:
        print(i, end="")
print("\n\nLa suma de los numeros es: ",str(suma))