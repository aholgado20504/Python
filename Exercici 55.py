def mostrar_parells():
    for i in range(2, 101, 2):
        print(i, end=" ")
    print()

def mostrar_senars():
    for i in range(1, 101, 2):
        print(i, end=" ")
    print()

if __name__ == "__main__":
    print("Parells fins 100:")
    mostrar_parells()
    print("Senars fins 100:")
    mostrar_senars()
