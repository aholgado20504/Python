import random

def hi_ha_duplicats(lista: list[int]) -> bool:
    """Retorna True si la llista té algun valor duplicat."""
    vistos = set()
    for x in lista:
        if x in vistos:
            return True
        vistos.add(x)
    return False

def llista_20_elements() -> list[int]:
    return [random.randint(1, 100) for _ in range(20)]

if __name__ == "__main__":
    l = llista_20_elements()
    print(l)
    print("Hi ha duplicats?" , hi_ha_duplicats(l))
