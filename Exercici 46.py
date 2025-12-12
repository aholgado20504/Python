def digits_parells(n: int) -> list[int]:
    return [int(d) for d in str(abs(n)) if int(d) % 2 == 0]

if __name__ == "__main__":
    n = int(input("Introdueix un número: "))
    parells = digits_parells(n)
    print("Dígits parells:", parells)