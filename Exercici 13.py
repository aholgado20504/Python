# calculadora que permeti utilitzar totes les operacions en números enters i de punt flotant.
numero = input("Vols treballar amb nombres enters o de punt flotant? (e/f): ").lower()
if numero == 'e':
    num1 = int(input("Introdueix el primer nombre enter: "))
    num2 = int(input("Introdueix el segon nombre enter: "))
elif numero == 'f':
    num1 = float(input("Introdueix el primer nombre de punt flotant: "))
    num2 = float(input("Introdueix el segon nombre de punt flotant: "))
operacio = input("Introdueix l'operació que vols realitzar (+, -, *, /): ")
if operacio == '+':
    resultat = num1 + num2
elif operacio == '-':
    resultat = num1 - num2
elif operacio == '*':
    resultat = num1 * num2
elif operacio == '/':
    if num2 != 0:
        resultat = num1 / num2
    else:
        resultat = "Error: Divisió per zero no permesa."
else:
    resultat = "Error: Operació no vàlida."
print("El resultat és:", resultat)