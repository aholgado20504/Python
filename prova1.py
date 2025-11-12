#Prova d'entrada de dades i operacions bàsiques
a = float(input("Escriu el primer nombre: "))
b = float(input("Escriu el segon nombre: "))
c = float(input("Escriu el terçer nombre: "))
d = a + b + c
print("La suma {} + {} + {} és {}".format(a, b, c, d))
if d > 20:
    print("La suma és major que 20, ja que és {}".format(d))
else:
    print("La suma no és major que 20, ja que és {}".format(d))

d = a * b * c
print("La multiplicació {} * {} * {} és {}".format(a, b, c, d))
if d > 100:
    print("La multiplicació és major que 100, ja que és {}".format(d))
else:
    print("La multiplicació no és major que 100, ja que és {}".format(d))