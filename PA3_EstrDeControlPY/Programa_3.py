#PROGRAMA QUE IMPRIME LA SIGUIENTE SUCESION: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100

for i in range(1,11):
    if i < 10:
        print(str(i**2), end=", ")
    else:
        print(str(i**2))