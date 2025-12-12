import random
import time

def intro():
    print("""En una època on els gegants governen Menorca. Nosaltres necessitem menjar,
Estem seguint el rastre de l'olor del menjar, però ens trobem en una cruïa.
Al final de cada camí hi ha un talaiot, en un viuen els gegants bons que ens convidaran
i en l'altre són uns caníbals afamats, i ens menjaran just ens vegin.
""")

def canviTalaiot():
    talaiot = ""
    while talaiot not in ("1", "2"):
        talaiot = input("A quin talaiot vols anar? Introdueix 1 o 2: ")
    return talaiot

def trobada(talaiot_escollit: str) -> bool:
    print("T'estàs apropant al talaiot...")
    time.sleep(1)
    print("Està fosc i és tenebrós...")
    time.sleep(1)
    print("Un gran gegant salta davant teu, t'agafa i ...")
    time.sleep(1)
    gegantamic = random.randint(1, 2)
    if talaiot_escollit == str(gegantamic):
        print("Et convida a menjar...")
        return True
    else:
        print("Se't menja d'un mos... ÑAMÑAMÑAM")
        return False

if __name__ == "__main__":
    punts = 0
    partidaNova = "si"
    while partidaNova.lower() in ("s", "si"):
        intro()
        nTalaiot = canviTalaiot()
        guanya = trobada(nTalaiot)
        if guanya:
            punts += 1
            print(f"Has guanyat aquesta ronda! Punts acumulats: {punts}")
        else:
            print("Has perdut la partida.")
            break
        partidaNova = input("Vols tornar a menjar (jugar)? Introdueix si o no: ")
        print("\n")
    print(f"Punts totals aconseguits: {punts}")
