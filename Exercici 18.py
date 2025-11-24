def es_vocal(caracter):
    vocals = "aeiouAEIOUàáèéìíóòúùÀÁÉÈÌÍÓÒÚÙ"
    if caracter in vocals and len(caracter) == 1:
        return True
    else:
        return False
# Proves de la funció es_vocal
caracter = input("Escriu una lletra i esbrinaré si és vocal o no: ")
print(es_vocal(caracter))