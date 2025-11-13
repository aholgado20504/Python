def gran():
    num1 = float(input("Introdueix el primer número: "))
    num2 = float(input("Introdueix el segon número: "))
    if num1 > num2:
        return num1
    else:
        return num2
resultat = gran()
# extra
print("El número més gran és:", resultat)
