def concat_amb_connector(ll1: list[str], ll2: list[str], connector: str) -> list[str]:
    return [a + connector + b for a, b in zip(ll1, ll2)]

if __name__ == "__main__":
    l1 = ["sub", "toyota"]
    l2 = ["campió", "supra"]
    print(concat_amb_connector(l1, l2, "-"))