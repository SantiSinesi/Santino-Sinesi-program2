a = int(input("Numero mayor que 2: "))
i = 2
while a % i != 0:
    i += 1
if i == a:
    print(str(a) + " primo")
else:
    print(str(a) + " no es primo")
