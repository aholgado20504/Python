import random

def generar_codi() -> str:
    return "".join(str(random.randint(0, 9)) for _ in range(4))

def analitzar_intent(codi: str, intent: str) -> tuple[int, int]:
    correctes = 0
    coincidencies = 0
    codi_lliure = []
    intent_lliure = []

    for c, i in zip(codi, intent):
        if c == i:
            correctes += 1
        else:
            codi_lliure.append(c)
            intent_lliure.append(i)

    for i in intent_lliure:
        if i in codi_lliure:
            coincidencies += 1
            codi_lliure.remove(i)

    return correctes, coincidencies

if __name__ == "__main__":
    codi_secret = generar_codi()
    # print(codi_secret)  # descomenta per fer proves
    encertat = False
    while not encertat:
        intent = input("Introdueix un codi de 4 xifres: ")
        if len(intent) != 4 or not intent.isdigit():
            print("Has d'introduir exactament 4 dígits.")
            continue
        correctes, coincidencies = analitzar_intent(codi_secret, intent)
        print(f"Números encertats (posició correcta): {correctes}")
        print(f"Números que coincideixen però en altra posició: {coincidencies}")
        if correctes == 4:
            print("Has endevinat el codi!")
            encertat = True