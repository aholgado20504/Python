def suma_quadrats_salt4(n: int) -> int:
    suma = 0
    for x in range(n - 4, 0, -4):
        suma += x ** 2
    return suma

if __name__ == "__main__":
    n = int(input("Introdueix un número menor de 100: "))
    if n >= 100:
        print("Ha de ser menor de 100.")
    else:
        print(f"Suma de quadrats: {suma_quadrats_salt4(n)}")