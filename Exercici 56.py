def suma_interval(a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))

if __name__ == "__main__":
    x = int(input("Primer número: "))
    y = int(input("Segon número: "))
    print("Suma:", suma_interval(x, y))