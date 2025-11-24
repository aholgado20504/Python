a = [10,9,8,7,6,5,1,2,3,4,]
# passar els elements de la llista a string
for i in range(len(a)):
    a[i]=str(a[i])
# crear un únic string separat per guió
print("-".join(a))





"""a = [10,9,8,7,6,5,1,2,3,4]
print(a[::-1]) #retorna una llista invertida, pero no modifica l'original
print(a)
a.reverse() # no retorna res, però modifica la liista original
print(a)"""










"""
a = [1, "a", "Capça", [2]]
a.append(10)
a.append("Cadena nova")
a.append([10,11,12])
a.extend([10,"Cadena nova",[10,11,12]])
a.insert(0,[3,2])
print(a)
"""
