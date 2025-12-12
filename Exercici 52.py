def crear_llista_fitxer(nom_fitxer: str) -> list[str]:
    paraules = []
    with open(nom_fitxer, "r", encoding="utf-8") as f:
        for linia in f:
            paraules.extend(linia.split())
    return paraules

if __name__ == "__main__":
    nom = input("Introdueix el nom del fitxer: ")
    try:
        llista = crear_llista_fitxer(nom)
        print(llista)
    except FileNotFoundError:
        print("El fitxer no existeix.")
