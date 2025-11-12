# Llegir una edat i imprimir si es major d'edat, no es major d'edat o exactament 18 anys.
edat = int(input("Introdueix la teva edat: "))
if edat > 18:
    print("Ets major d'edat.")
elif edat < 18:
    print("Ets menor d'edat.")
else:
    print("Tens exactament 18 anys.")