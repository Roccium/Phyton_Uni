import math
def count_vowels(parola):
    count=0
    for x in range(len(parola)):
        if parola[x] in ["a","e","i","o","u","A","E","I","O","U"]:
            count = count+1
    return count

def max_lenght_s(l_stringhe ):
    max = -math.inf
    index=""
    for x in range(len(l_stringhe)):
        if(len(l_stringhe[x])>=max):
            max=len(l_stringhe[x])
            index=x
    return x
def max_min(l):
    print(l)
    max= -math.inf
    min = math.inf
    for x in range(len(l)):
        if l[x]< min:
            min=l[x]
        if l[x]>max:
            max=l[x]
    return [max,min]
def all_one(l):
    for x in range(len(l)):
        for y in range(len(l[x])):
            l[x][y]=1
    return l
def all_zero(l):
    for x in range(len(l)):
        for y in range(len(l[x])):
            l[x][y]=0
    return l
def sup_inf_0(l):
    for x in range(len(l)):
        for y in range(len(l[x])):
            if(x==0 or x==(len(l)-1)):
                l[x][y]=0
    return l

def right_left_1(l):
    for x in range(len(l)):
        for y in range(len(l[x])):
            if(y==0 or y==(len(l[x])-1)):
                l[x][y]=1
    return l
def sum(l):
    sum=0
    for x in range(len(l)):
            for y in range(len(l[x])):
                    sum=sum+l[x][y]
    return sum
def approx_integrale(f,min,Max):
    N= abs(Max-min) *100
    for x in range(N):
        f.replace("x",x)
        print(f)
def tris():
    turno=0
    simboli=["X","O"]
    l=list(range(3))
    for i in range(len(l)):
        l[i]=list(range(3))
    all_zero(l)
    print(l)
    while True:
        a,b = input("inserire le coordinate delle mosse").split(",")
        a=int(a)-1
        b=int(b)-1
        if(l[a][b]!=0):
            print("già occupato")
        else:
            l[a][b]=simboli[turno]
        turno= (turno+1)%2
        print(l)
        
def main ():
    tris()


    '''
    f= input("inserire la funzione formato mx+q: ")
    a,b= input("inserire intervallo a,b ").split(",")
    approx_integrale(f,int(a),int(b)) non completato


    x= int(input("inserire dimensioni tabella(x): "))
    y= int(input("inserire dimensioni tabella(y): "))
    l=list(range(x))
    for i in range(len(l)):
        l[i]=list(range(y))
    print(l)
    all_one(l)
    sup_inf_0(l)
    right_left_1(l)
    print(l)
    print("somma totale: ",sum(l))
    
 
    i=0
    L=[]
    while i!=" ":
        i=input("inserire numeri, o " " per fermarsi")
        if(i!=" "):
            L.append(int(i))
    print(max_min(L))
    
    a=int(input("quante stringhe inserire: "))
    l_stringhe=[]
    for x in range(a):
        l_stringhe.append(str(input("inserire stringhe: ")))
    print(l_stringhe[max_lenght_s(l_stringhe)])

    a= input("inserire stringa: ")
    n_vocali=count_vowels(a)
    print(n_vocali)
    '''
main()