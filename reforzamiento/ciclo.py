print(f"Holas")
def serieFibonaci():
    nI=0
    nS=1
    n=int(input("Introduce el N numero:"))
    cont=1
    print(nI)
    while(cont<n):
        print(nS)
        nT=nS+nI
        nI=nS
        nS=nT
        cont=cont+1

def fibonaciN():
    nI=0
    nS=1
    n=int(input("Introduce el N numero:"))
    cont=1    
    if(n>1):        
        while(cont<n):
            nT=nS+nI
            nI=nS
            nS=nT
            cont=cont+1
    else:
        nS=n
    print(f"el fibonaci de {n} es {nS}")

#serieFibonaci()
#fibonaciN()

def siNumeroPrimo():
    num=int(input("Ingrese un numero:"))
    cont=1
    cantDiv=0
    while(cont<=num):
        if(num%cont==0):
            cantDiv=cantDiv+1
        cont=cont+1
    if(cantDiv==2):
        print(f"El numero {num} es primo")
    else:
        print(f"El numero {num} no es primo")


#siNumeroPrimo()

def num_primo():
    num=int(input("Ingrese el limite maximo"))
    numx=1
    while (numx<=num):
        cont=1
        cantDiv=0
        while(cont<=numx):
            if(numx%cont==0):
                cantDiv=cantDiv+1
            cont=cont+1
        if(cantDiv==2):
            print(f"El numero {numx} es primo")
         #else:
            #print(f"El numero {num} no es primo")
        numx=numx + 1

num_primo()