def menu_princial():
    opcio = 0
    while opcio<1 or opcio>3:
        opcio = int(input(""" Elegeixi una opció:
                        1. Calculadora decimal
                        2. Calculadora real(floats)
                        3. Sortir \n"""))
        if opcio>0 and opcio<4:
            return opcio
        else:
            print("Opció no vàlida, torna a provar!!\n")
            return menu_princial()

def menu_calculadora():
    opcio=0
    while opcio<1 or opcio>5:
        opcio = int(input(""" Elegeixi una operació:
                    1. Suma
                    2. Resta
                    3. Multiplicació
                    4. Divisió
                    5. Sortir \n"""))
        if opcio>0 and opcio<6:
            return opcio
        else:
            print("Operació no vàlida, torna a provar!!\n")
            return menu_calculadora()
# Calculadora decimal

def calculadora_decimal(opcio):
    num1=float(input("Introdueix el primer número real: "))
    num2=float(input("Introdueix el segon número real: "))
    match(opcio):
        case 1:
            print("Estic pensant la suma!")
            print("El resultat de la suma és:", num1+num2)
        case 2:
            print("Estic pensant la resta!")
            print("El resultat de la resta és:", num1-num2)
        case 3:
            print("Estic pensant la multiplicació!")
            print("El resultat de la multiplicació és:", num1*num2)
        case 4:
            print("Estic pensant la divisió!")
            if num2!=0:
                print("El resultat de la divisió és:", num1/num2)
            else:
                print("Error: Divisió per zero no permesa. Ets tonto?")
        case 0:
            print("Sortint de la calculadora decimal.")
        case _:
            print("Operació no vàlida.")

# Calculadora real
def calculadora_real(opcio):
    num1=float(input("Introdueix el primer número real: "))
    num2=float(input("Introdueix el segon número real: "))
    match(opcio):
        case 1:
            print("Estic pensant la suma!\n")
            print("El resultat de la suma és:", num1+num2)
        case 2:
            print("Estic pensant la resta!")
            print("El resultat de la resta és:", num1-num2)
        case 3:
            print("Estic pensant la multiplicació!")
            print("El resultat de la multiplicació és:", num1*num2)
        case 4:
            print("Estic pensant la divisió!")
            if num2!=0:
                print("El resultat de la divisió és:", num1/num2)
            else:
                print("Error: Divisió per zero no permesa. Ets tonto?")
        case 0:
            print("Sortint de la calculadora real.\n")
        case _:
            print("Operació no vàlida.")

# Programa principal
op = 1
while op!=0:
    op = menu_princial()
    if op==1:
        # Calculadora decimal
        print("Estic passant per sa calculadora decimal")
        calculadora_decimal(menu_calculadora())
    elif op==2:
        # Calculadora real
        print("Estic passant per sa calculadora real")
        calculadora_real(menu_calculadora())
    else:
        print("Gràcies per emprar sa meva calculadora, fins prest\n")
        op=0
