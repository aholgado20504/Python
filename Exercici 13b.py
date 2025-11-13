# calculadora que permet utilitzar totes les operacions en números enters i de punt flotant. funcionalitat que perment treballar amb canvis de base (binari, octal, decimal i hexadecimal).
base = int(input("Introdueix la base numèrica (2-binari, 8-octal, 10-decimal, 16-hexadecimal): "))
num1 = input("Introdueix el primer número: ")
num2 = input("Introdueix el segon número: ")
if base == 2:
    num1 = int(num1, 2)
    num2 = int(num2, 2)
elif base == 8:
    num1 = int(num1, 8)
    num2 = int(num2, 8)
elif base == 16:
    num1 = int(num1, 16)
    num2 = int(num2, 16)
else:
    num1 = float(num1)
    num2 = float(num2)
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
if base == 2:
    print("Resultat en binari:", bin(int(resultat)))
elif base == 8:
    print("Resultat en octal:", oct(int(resultat)))
elif base == 16:
    print("Resultat en hexadecimal:", hex(int(resultat)))
else:
    print("Resultat en decimal:", resultat)

# Me cago en la puta