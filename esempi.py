a = input("Inserisci il valore A: ")
b = input("Inserisci il valore B: ")
c = input("Inserisci il valore C: ")
a = int(a)
b = int(b)
c = int(c)

'''
while True:
    x = input()
    if True:
        break
'''
print("A =",a,"B =",b,"C =",c)
intdict = {"A":a,"B":b,"C":c}
sorted_by_values = dict(sorted(intdict.items(), key=lambda item: item[1],reverse=True))
print(sorted_by_values.items())
mag_key = list(sorted_by_values)[0]
print("l'elemento maggiore è : "+mag_key+" di valore "+ str(sorted_by_values.get(mag_key)) )

