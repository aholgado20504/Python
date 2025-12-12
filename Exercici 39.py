def comprovar_rima(p1: str, p2: str) -> str:
    p1 = p1.lower()
    p2 = p2.lower()
    if len(p1) < 2 or len(p2) < 2:
        return "No rimen."
    if p1[-3:] == p2[-3:] and len(p1) >= 3 and len(p2) >= 3:
        return "Rimen."
    elif p1[-2:] == p2[-2:]:
        return "Rimen un poc."
    else:
        return "No rimen."

if __name__ == "__main__":
    paraula1 = input("Introdueix la primera paraula: ")
    paraula2 = input("Introdueix la segona paraula: ")
    print(comprovar_rima(paraula1, paraula2))