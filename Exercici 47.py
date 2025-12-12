def eliminarcapicua(llista: list) -> list:
    if len(llista) <= 2:
        return []
    return llista[1:-1]

if __name__ == "__main__":
    print(eliminarcapicua([1, 2, 3, 4]))