a = int(input("Altura del triangulo: "))
for i in range(1, a+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")
