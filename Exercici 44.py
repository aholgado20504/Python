if __name__ == "__main__":
    n = int(input("Introdueix un número (1 a 20): "))
    if 1 <= n <= 20:
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
    else:
        print("Número fora de rang.")