def noms_que_comencen_per(noms, lletra):
    comptador = 0
    for nom in noms:
        if nom.lower().startswith(lletra.lower()):
            comptador += 1
    return comptador

llista_noms = ["Aitor","Joan","Ibai","Moha","Albert","Iker","Aritz","Russell","Edgar","Justin","Raúl","Luca"]
lletra_usuari = input("Introdueix una lletra: ")
quantitat = noms_que_comencen_per(llista_noms, lletra_usuari)
print(f"Hi ha {quantitat} noms que comencen per '{lletra_usuari}'.")