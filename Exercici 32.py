def majorsque(valors, limit):
    print(f"Valors major que {limit}:")
    for v in valors:
        if v > limit:
            print(v)
n=int(input("Quants valors vols introduir? "))
llista=[]
for i in range(n):
    edat=int(input(f"Introdueix l'edat {i+1}: "))
    llista.append(edat)
#mostrar els que son majors d'edat.
edats=tuple(llista)
majorsque(edats, 18)