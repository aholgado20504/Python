def comptar_digits(n: int) -> int:
    return len(str(abs(n)))

if __name__ == "__main__":
    n = int(input("Introdueix un número (1 a 900000): "))
    if 1 <= n <= 900000:
        print(f"Té {comptar_digits(n)} dígits.")
    else:
        print("Número fora de rang.")