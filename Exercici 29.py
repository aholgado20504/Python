def lelo(ñoñas):
    recompte=0
    for c in ñoñas:
        if c.isupper():
            recompte += 1
    return recompte

print(lelo("Hola MON"))
print(lelo("no hi han majuscules"))
print(lelo("ABCIHNJG746ehjug"))