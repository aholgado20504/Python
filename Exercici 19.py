def sumar_llista(llista):
    suma = 0
    for num in llista:
        suma += num
    return suma

def multiplicar_llista(llista):
    multiplicacio = 1
    for num in llista:
        multiplicacio *= num
    return multiplicacio

# Proves de les funcions
print(sumar_llista([1, 2, 3, 4]))   # Ha de retornar 10
print(sumar_llista([5, 10, 15]))    # Ha de retornar 30
print(multiplicar_llista([1, 2, 3, 4])) # Ha de retornar 24
print(multiplicar_llista([2, 3, 4]))    # Ha de retornar 24
print(sumar_llista([-1, 1, -1, 1])) # Ha de retornar 0