def llista_a_diccionari(llista: list[str]) -> dict:
    return {valor: idx for idx, valor in enumerate(llista)}

if __name__ == "__main__":
    l = ["casa", "cotxe", "cadira", "taula"]
    print(llista_a_diccionari(l))