def lenp(frase: str) -> list[int]:
    paraules = frase.split()
    return list(map(len, paraules))

if __name__ == "__main__":
    f = input("Introdueix una frase: ")
    print(lenp(f))