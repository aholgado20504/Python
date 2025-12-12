def dividir(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: no es pot dividir per zero.")
        return None

if __name__ == "__main__":
    x = float(input("Numerador: "))
    y = float(input("Denominador: "))
    resultat = dividir(x, y)
    if resultat is not None:
        print("Resultat:", resultat)