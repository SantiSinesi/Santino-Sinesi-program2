cantidad = float(input("Cantidad a invertir: "))
interes = float(input("Interés porcentual anual: "))
Años = int(input("Años:"))
for i in range(Años):
    cantidad *= 1 + interes / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(cantidad, 2)))
