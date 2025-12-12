from functools import reduce

def Passar_a_Numero(llista: list[int]) -> int:
    return reduce(lambda acc, d: acc * 10 + d, llista, 0)

if __name__ == "__main__":
    print(Passar_a_Numero([3, 4, 1, 5]))