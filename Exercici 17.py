def longitud(element):
    contador = 0
    for _ in element:
        contador += 1
    return contador
var = longitud([1, 2, 3, 4, 5])
print("La longitud de la llista és:", var)
var = longitud([1, 3, 5 , 7, 9, 11, 13])
print("La longitud de la llista és:", var) 
var = longitud("Adeu, món!")
print("La longitud de la cadena és:", var)