num = [1,2,3,4,5,6,7]
def crear_punts(llista):
    for num in llista:
        print('.' * num)
crear_punts(list(range(1, num + 1)))