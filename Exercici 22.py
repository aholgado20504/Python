# Definir una funció superposicio() que agafi dues llistes i retorni vertader si hi ha un element en comú, en cas contrari, que retorni fals.
llista1 = input("Introdueix la primera llista d'elements separats per comes: ").split(',')
llista2 = input("Introdueix la segona llista d'elements separats per comes: ").split(',')
def superposicio(llista1, llista2):
    for element in llista1:
        if element in llista2:
            return True
        else:
            return False
    
print(superposicio(llista1, llista2))