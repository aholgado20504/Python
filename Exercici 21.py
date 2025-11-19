def es_palindrom(cadena):
    cadena_invertida = invertir(cadena)
    return cadena == cadena_invertida

def invertir(cadena):
    cadena_invertida = ""
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida

# Proves de la funció es_palindrom
print(es_palindrom("radar"))  # Ha de retornar True
print(es_palindrom("civic"))  # Ha de retornar True
print(es_palindrom("Python")) # Ha de retornar False
print(es_palindrom("refer"))  # Ha de retornar True
print(es_palindrom("hello"))  # Ha de retornar False
print(es_palindrom("Ana"))    # Ha de retornar False (considerant majúscules i minúscules)
print(es_palindrom("kumalala")) # Ha de retornar False