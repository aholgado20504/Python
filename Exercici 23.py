char = input("Introdueix un caràcter: ")
num = int(input("Introdueix quantes vegades el vols multiplicar: "))
def crear_repetits(num, char):
    return char * num
print(crear_repetits(num, char))