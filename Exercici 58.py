def elements_parells(llista: list[str]) -> list[str]:
    return [elem for idx, elem in enumerate(llista) if idx % 2 == 0]

if __name__ == "__main__":
    l = ["a", "b", "c", "d", "e"]
    print(elements_parells(l))