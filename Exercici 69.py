def primers_potencies(potencia: int) -> list[int]:
    return [n ** potencia for n in range(0, 10)]

if __name__ == "__main__":
    print(primers_potencies(2))
    print(primers_potencies(3))