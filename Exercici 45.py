def suma_digits(n: int) -> int:
    return sum(int(d) for d in str(abs(n)))

if __name__ == "__main__":
    n = int(input("Introdueix un número: "))
    s = suma_digits(n)
    tipus = "parell" if s % 2 == 0 else "senar"
    print(f"La suma dels dígits és {s}, que és {tipus}.")