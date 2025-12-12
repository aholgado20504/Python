fitxer = "/home/cicles/AO/Prova/Ex12.txt"

llista_noms = []
with open(fitxer, "r", encoding="utf-8") as f:
    for linia in f:
        nom = linia.strip()  # treu salts de línia i espais
        if nom:
            llista_noms.append(nom)

print(llista_noms)