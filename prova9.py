def ordenar(x,y):
    if x>y:
        return x,y
    elif y>x:
        return y,x
    else:
        return x,y
v1=int(input("Introdueix el primer operador: "))
v2=int(input("Introduieix el segon operador: "))
v1, v2 = ordenar(v1,v2)
for e in range(v2,v1+1):
    if e%2!=0:
        print(e)




"""v1 = int(input("introduex un nombre: "))
v2 = int(input("introdueix un altre nombre: "))
r = (v1*v2) // 2

for i in range(r,-1,-1):
    print(i)"""