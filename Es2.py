import math
'''
a = input("Inserisci il primo valore: ")
b = input("Inserisci il secondo valore: ")
a = int(a)
b = int(b)
print(a+b);
print(a-b);
print(a*b);
print((a+b)/2);
#distanza
print(abs(a-b));
print("il valore massimo è ",max(a,b))
print("il valore minimo è ", min(a,b))


print("scrivere i valori per le restistenze per il circuito R1 serie (R2 parallelo R3)")
R1 = int(input("Inserisci R1 in Ω: "))
R2 = int(input("Inserisci R2 in Ω: "))
R3 = int(input("Inserisci R2 in Ω: "))
Rtot = R1+((R2*R3)/(R1+R2))
print(Rtot)


# da chiedere se devo tenerlo numero
import random
Rnd = str(random.randrange(1000,10000))
for x in Rnd:
    print (x);

#vara se riesci a fare con API
prezzi = []
for x in range(2):
    costo=float(input("Inserisci il costo di un auto nuova: "))
    stima_km=float(input("Inserisci una stima dei kilometri percorsi in un anno: "))
    costo_carburante=float(input("Inserisci il costo del carburante: "))
    km_l=float(input("Inserisci l'efficenza in chilometri al litro: "))
    costo_dopo5_anni=float(input("Inserisci una stima del prezzo di rivendita dopo cinque anni: "))
    costo_tot = costo+ ((stima_km*5/km_l)*costo_carburante)-costo_dopo5_anni
    prezzi.append(costo_tot)

if(prezzi[0]>prezzi[1]):
    print("la prima opzione è migliore della seconda")
else:
    print("la seconda opzione è migliore della prima")

    

Q1=float(input("Q1: "))
Q2=float(input("Q2: "))
r =float(input("distanza : "))
ε= 8.854e-12
print("F = ",((Q1*Q2)/4*math.pi*ε))

s1 = "aquilone"
s2 = "casa"

print(s2[0]+s2[1]+s2[2]+"..."+s2[-3]+s2[-2]+s2[-1])

for x in range(3):
    print (s1[x])
print("...")
for x in range(3):
    print (s1[-(x+1)]);

num_tel = str(input("inserire numero telefonico da formattare: "))

print("("+num_tel[:3]+")    "+num_tel[3:6]+"-"+num_tel[6:10])
'''
a = input("Inserisci il primo valore: ")
b = input("Inserisci il secondo valore: ")
a = int(a)
b = int(b)
print(a+b);
print(a-b);
print(a*b);
print((a+b)/2);
#distanza
print(abs(a-b));
print("il valore massimo è ",max(a,b))
print("il valore minimo è ", min(a,b))
'''
print(f'{s:20}’)  stampa su 20 caratteri allineati a sinistra Paul________________
print(f'{s:>20}’)  stampa su 20 caratteri allineati a destra ________________Paul
print(f’{x:10}’)  stampa su 10 caratteri allineati a destra ________10
print(f’{z:10.3f}’) stampa su ALMENO 10 caratteri con 3 cifre dopo la virgola ______3.24
'''