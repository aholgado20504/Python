# Definir una funció invertir() que calculi la inversa d’una cadena. Ex: invertir(“Soc del Ramis”) hauria de tornar la cadena “simaR led coS”.
def invertir(cadena):
    cadena_invertida = ""
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida

# Proves de la funció invertir
print(invertir("Soc del Ramis"))    # Ha de retornar "simaR led coS"
print(invertir("Python"))   # Ha de retornar "nohtyP"
print(invertir("12345"))    # Ha de retornar "54321"
