num = int(input("Introdueix quants punts vols a la llista: "))
def crear_punts(llista):
    for num in llista:
        print('.' * num)
crear_punts(list(range(1, num + 1)))