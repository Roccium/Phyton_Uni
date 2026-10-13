import math
'''
print(1==1)
print(1==1.0)
print(2.0== math.sqrt(4))
print("1"==1)
print("caio"=="Ciao")

a = input("Inserisci il  valore: ")
if len(a)>0:
    if a.isalpha() :
        print("la frase contiene solo lettere")
    else:
        print("la frase non contiene solo lettere")
    if a.isupper() :
        print("la frase contiene solo lettere maiuscole")
    else:
        print("la frase non contiene solo lettere maiuscole")
    if a.islower() :
        print("la frase contiene solo lettere minuscole")
    else:
        print("la frase non contiene solo lettere minuscole")
    if (a.isdigit() and a.isalpha()) :
        print("la frase contiene solo lettere e cifre")
    else:
        print("la frase non contiene solo lettere e cifre")
    if a.endswith(".") :
            print("la frase finisce con .")
    else:
        print("la frase non finisce con .")
    if a[0].isupper() :
            print("la frase inizia con una lettera maiuscola")
    else:
        print("la frase non inizia con una lettera maiuscola")
   #da fare a casetta / dopo     
    if ("." in a):
        print("la frase inizia con una lettera maiuscola")
    else:
        print("la frase non inizia con una lettera maiuscola")

a = input("Inserisci il primo valore: ")
b = input("Inserisci il secondo valore: ")
if a.isalpha and b.isalpha:
    if(b in a):
        print("la sequenza lunga contiene la corta")
        print("primo indice dove è stata trovata ", a.find(b))
        print("la seconda stringa era presente :",a.count(b)," nella prima")
    else:
        print("non era presente la strina")
else:
    print("dare in input stringhe")

x=0.0
max = -(math.inf)
min = math.inf
disp=0
pari=0
while True:
    a = input("Inserisci il  valore: ")
    if (not a.isalnum()):
        break
    else:
        a=float(a)
        x=x+a
        if a%2==0:
            pari=pari+1
        else:
            disp=disp+1
        if a>max:
            max= a
        if a<min:
            min = a
        print(x,"I","massimo :",max,"minimo :",min,"numeri pari :",pari,"numeri dispari:",disp)

velocita = float(input("velocita di lancio in km/h: "))
vdf = math.sqrt((2.2e14*6.67e-11*2)/11e3)
if velocita<vdf:
    print("la cometa ti tiene")
else:
    x=((velocita**2)*11000)/(2*6.67e-11)-2.2e14
    print("alla cometa mancano: ",x,"kili")
 '''
anno = int(input("anno maggiore del 1582: "))
if ((not (anno%100==0))and(anno%4==0))or( (not (anno%100==0)) and (anno%400==0)):
    print("l'anno è bisestile")
else:
    print("l'hanno non è bisestile")