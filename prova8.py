def ordenar(x,y):
#Prec: DOnats dos números
#Post: Els retorna amb ordre, primer el major i després el menor
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
    print(e)




"""r=v1==v2
print(r)
r=v1!=v2
print(r)
r=v1>v2
print(r)
r=v1<v2
print(r)
r=v1>=v2
print(r)
r=v1<=v2
print(r)"""


""""r=v1+v2
print(r)
r=v1-v2
print(r)
r=v1*v2
print(r)
r=v1//v2 #Divisió entera
print(r)
r=v1/v2 #Divisió real
print(r)
r=v1%v2
print(r)
r=v1**v2
print(r)
r= v1*v2**2/v1-v1%v2
print(r)"""