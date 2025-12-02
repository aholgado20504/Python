def noms_que_comencen_per(noms, lletra="a"):
    comptador = 0
    for nom in noms:
        if nom.lower().startswith(lletra.lower()):
            comptador += 1
    return comptador

# Exemples
llista=["Aitor","Joan","iker","Moha","Albert","Iker","Aritz"]
print(noms_que_comencen_per(llista))
