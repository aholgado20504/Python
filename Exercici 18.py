def es_vocal(caracter):
    vocals = "aeiouAEIOUàáèéìíóòúù"
    if caracter in vocals and len(caracter) == 1:
        return True
    else:
        return False
# Proves de la funció es_vocal
print(es_vocal("a"))  # Ha de retornar True
print(es_vocal("E"))  # Ha de retornar True
print(es_vocal("b"))  # Ha de retornar False
print(es_vocal("O"))  # Ha de retornar True
print(es_vocal("z"))  # Ha de retornar False
print(es_vocal("ae")) # Ha de retornar False (perque n'hi han més d'un caràcter)