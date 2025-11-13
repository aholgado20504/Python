# Escriure una calculadora que permeti utilitzar totes les operacions en números enters i de punt flotant.
numero = input("Vols emprar números enters (i) o de punt flotant (f)? ")
if numero == 'i':
    num1 = int(input("Introdueix el primer número enter: "))
    num2 = int(input("Introdueix el segon número enter: "))
elif numero == 'f':
    num1 = float(input("Introdueix el primer número de punt flotant: "))
    num2 = float(input("Introdueix el segon número de punt flotant: "))
else:
    print("Tipus de número no vàlid.")
    exit()
operacio = input("Introdueix l'operació (+, -, *, /, //, %, **): ")
if operacio == '+':
    resultat = num1 + num2
elif operacio == '-':
    resultat = num1 - num2
elif operacio == '*':
    resultat = num1 * num2
elif operacio == '/':
    resultat = num1 / num2
elif operacio == '//':
    resultat = num1 // num2
elif operacio == '%':
    resultat = num1 % num2
elif operacio == '**':
    resultat = num1 ** num2
else:
    resultat = "Operació no vàlida"
print("El resultat és:", resultat)