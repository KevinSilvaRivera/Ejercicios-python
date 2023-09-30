#PROGRAMA QUE PIDE LA ALTURA EN METROS DE 8 PERSONAS E IMPRIME: “APTOS”, SI EL PROMEDIO DE ELLAS ES MAYOR O IGUAL A 1.75 METROS, Y “NO APTOS”, EN CASO CONTRARIO

promedio=0
print("Ingrese las estaturas en metros de 8 personas ")
for i in range(8):
    print(str(i+1),"._", end=" ")
    estatura=float(input())
    promedio=promedio+estatura

promedio=promedio/8
if promedio >= 1.75:
    print("APTOS, el promedio de las alturas es: ",str(promedio), " metros")
else:
     print("NO APTOS, el promedio de las alturas es: ",str(promedio), " metros")