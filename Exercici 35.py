def comptar_vocals(paraula):
    paraula = paraula.lower()
    comptadors = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for lletra in paraula:
        if lletra in comptadors:
            comptadors[lletra] += 1
    return comptadors
#Exemple
r = comptar_vocals("Ratapinyada")
print(f"Hi ha {r['a']} a's, {r['e']} e's, {r['i']} i's, {r['o']} o's i {r['u']} u's")