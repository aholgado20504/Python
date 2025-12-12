def comptar_coincidencies(llista: list[int]) -> int:
    return sum(1 for idx, valor in enumerate(llista) if idx == valor)

if __name__ == "__main__":
    print(comptar_coincidencies([0, 2, 3, 3, 4]))