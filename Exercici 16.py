# Definir una funció gran_de_tres(), donats tres números, retorni el major. Prova-la amb diferents exemples.
def gran_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

var = gran_de_tres(10, 20, 15)
print("El major és:", var)
var = gran_de_tres(-5, -10, -1)
print("El major és:", var)
var = gran_de_tres(6, 7, 4)
print("El major és:", var)