def filtre(paraules,x):
    return [p for p in paraules if len(p)>x]
llista = ["Hola", "Ramis", "IES", "Paraula"]
print(filtre(llista, 4))