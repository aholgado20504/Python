def hi_ha_duplicats(llista: list) -> bool:
    return len(llista) != len(set(llista))

if __name__ == "__main__":
    print(hi_ha_duplicats([1, 2, 3, 3]))
    print(hi_ha_duplicats([1, 2, 3]))