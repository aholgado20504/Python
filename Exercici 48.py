def esta_ordenada(llista: list[int]) -> str:
    if llista == sorted(llista):
        return "està ordenada de forma ascendent"
    elif llista == sorted(llista, reverse=True):
        return "està ordenada de forma descendent"
    else:
        return "no està ordenada"

if __name__ == "__main__":
    print(esta_ordenada([3, 2, 1]))
    print(esta_ordenada([4, 5, 6]))
    print(esta_ordenada([3, 1, 2]))