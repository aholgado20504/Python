# Llegir una edat i imprimir si es major d'edat, no es major d'edat o exactament 18 anys.
def majoredat(edat):
    if edat > 18:
        return "Ets major d'edat."
    elif edat < 18:
        return "No ets major d'edat."
    else:
        return "Tens exactament 18 anys."
edat = int(input("Introdueix la teva edat: "))
majoredat(edat)
edat = int(input("Introdueix la teva edat: "))
majoredat(edat)