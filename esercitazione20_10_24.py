"""
a = input("Inserisci il  valore: ")
dove=[]
b=""
i=0
for x in range(len(a)):
    if(x%2==0):
        print(a[x])
    if(a[x].isupper()):
        print(a[x])
    if(a[x].isdigit()):
        i=i+1
    if(a[x] in ["a","e","i","o","u","A","E","I","O","U"]):
        b=b+"_"
        dove.append(x)
    else:
        b=b+a[x]
        
print(b)
print(i)
print(dove)

b= int(input("Inserisci il  valore(solo numeri interi): "))
div=2
print(range(b))

while b>1:
    if(b%div==0 ):
       print(div)
       b=b/div
    else:
        div=div+1
   
  
   ##scritto da schifo     
s=0
v = int(input("velocita iniziale m/s: "))
sec = float(input("secondi che si voglioni simulare int: "))
DT=0.01
for x in range(int(sec/DT)):
    s=s+(v*DT)
    v=v-(9.81*DT)
    if(x%100==0):
        print(s)
    if(s<0):
        break

 
To = int(input("temperatura iniziale dell'oggetto: "))
Ta = int(input("temperatura dell' ambiente: "))
k = float(input("il valore dalla costante k: "))
np = int(input("il numero di periodi che si desidera simulare: "))
Tn=0
stop=(To/100)*30
for x in range(np):
    To=To-k*(To-Ta)
    print(To)
    if(To<stop):
        break

"""
import math
star = int(input("numero di cui fare la radice: "))
rad= math.trunc(star/2)
for x in range(20):
    rad=(1/2)*(rad+(star/rad))
    print(rad)