def llegir_fitxer(nom_fitxer: str) -> str | None:
    try:
        with open(nom_fitxer, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Error: el fitxer no existeix.")
    except OSError:
        print("Error: no s'ha pogut obrir el fitxer.")
    return None

if __name__ == "__main__":
    nom = input("Nom del fitxer: ")
    contingut = llegir_fitxer(nom)
    if contingut is not None:
        print("Contingut del fitxer:")
        print(contingut)