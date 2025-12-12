def index_paraula(llista_ordenada: list[str], paraula: str) -> int:
    try:
        return llista_ordenada.index(paraula)
    except ValueError:
        return -1

if __name__ == "__main__":
    l = ["casa", "cotxe", "moix", "ca"]
    p = input("Paraula a cercar: ")
    print(index_paraula(l, p))