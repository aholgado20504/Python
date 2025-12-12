def es_primer(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    primers = [n for n in range(1, 101) if es_primer(n)]
    print("Números primers:", primers)
    print("Quantitat:", len(primers))