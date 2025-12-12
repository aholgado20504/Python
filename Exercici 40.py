def capital_final(c_inicial: float, interes: float, anys: int) -> float:
    return c_inicial * (1 + interes / 100) ** anys

if __name__ == "__main__":
    while True:
        c = float(input("Quantitat (50_000 a 800_000): "))
        if 50000 <= c <= 800000:
            break
        print("Quantitat fora de rang.")
    while True:
        i = float(input("Interès (0.5 a 13): "))
        if 0.5 <= i <= 13:
            break
        print("Interès fora de rang.")
    while True:
        a = int(input("Anys (3 a 40): "))
        if 3 <= a <= 40:
            break
        print("Anys fora de rang.")
    cf = capital_final(c, i, a)
    print(f"Capital final: {cf:.2f} €")