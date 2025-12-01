def paraula_mes_llarga(llista):
    return max(llista,key=len)
print(paraula_mes_llarga(["Hola", "Ramis", "IES", "Paraula"]))