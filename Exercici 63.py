def filtrar_paraules(llista: list[str], lletra: str) -> list[str]:
    lletra = lletra.lower()
    return list(filter(lambda p: p.lower().startswith(lletra), llista))

if __name__ == "__main__":
    l = ["maria", "manta", "peu", "mà"]
    print(filtrar_paraules(l, "m"))