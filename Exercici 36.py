def es_de_traspas(any: int) -> bool:
    return (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0)

if __name__ == "__main__":
    a = int(input("Introdueix un any: "))
    if es_de_traspas(a):
        print(f"L'any {a} és de traspàs.")
    else:
        print(f"L'any {a} no és de traspàs.")
