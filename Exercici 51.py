def elimina_duplicats(llista: list) -> list:
    vistos = set()
    resultat = []
    for elem in llista:
        if elem not in vistos:
            vistos.add(elem)
            resultat.append(elem)
    return resultat

if __name__ == "__main__":
    print(elimina_duplicats([1, 2, 2, 3, 1, 4]))