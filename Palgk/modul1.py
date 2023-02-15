def Kustuta(i:list,p:list,):
    kesk_palk=sum(p)/len(p)
    print(kesk_palk)
    v=int(input("Kellel palk 1- on suurem,2-on väiksem?"))
    if v==1:
        for palk in p:
            if palk>kesk_palk:
                ind=p.index(palk)
                print(ind)
                p.remove(palk)
                i.pop(ind)
    else:
        pass
    return i,p
def Lisa_andmed(i:list,p:list):
    """Kirjeldus....
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    n=int(input("Mitu inimest:"))
    for j in range(n):
        nimi=input("Sisesta nimi: ")
        palk=int(input("Sisesta palk: "))
        i.append(nimi)
        p.append(palk)
    return i,p
def Kustutamine(i:list,p:list):
    """Kirjeldus....
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    nimi=input("Sisesta nimi: ")
    if nimi in i:
        n=i.count(nimi)
        for j in range(n):
            ind=i.index(nimi)
            i.pop(ind)
            p.pop(ind)
    return i,p
def Suurim_palk(i:list,p:list):
    palk=max(p)
    ind=p.index(palk)
    nimi=i[ind]
    return palk,nimi
def Sorteerimine(i:list,p:list):
    v=int(input("palk 1-kahaneb,2-kasvab?"))
    if v==1:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]<p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=i[k]
                    i[k]=abi
    elif v==2:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]>p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=i[k]
                    i[k]=abi
    return i,p
def Vordsed_palgad(i:list,p:list):
    dublikatid=[x for x in p if p.count(x)>1 ]
    dublikatid=list(set(dublikatid))
    for palk in dublikatid: 
        n=p.count(palk)
        k=-1
        print(f"{palk} saavad kätte järgmised inimesed:")
        for j in range(n):            
            k=p.index(palk,k+1)
            nimi=i[k]
            print(nimi)
def maks(x:list,y:list): 
    im=[] 
    pm=[]
    ind=y.index(max(y))
    n=y.count(y[ind])
    if n!=1:
        print("Siin on mõned inimesed kes saab maksimaalne palk")
        kopia=y.copy()
        print("Saavad saama palk: ", end="")
        for i in range(n):
            print(f"{x[ind]}, ", end="") 
            kopia.pop(ind) 
            kopia.insert(ind,0)
            ind=kopia.index(max(kopia))
        vas=(f"ja nad saavad {max(y)}")
    else:
        vas=(f"Saab kõrgeimat palka {x[ind]} ja ta saab {y[ind]}")
    return vas
def leia_palga_summa(nimi, palgad, inimesed):
    summa = 0
    for i in range(len(inimesed)):
        if inimesed[i] == nimi:
            summa += palgad[i]
    return summa
def listok(x:list,y:list): 
    palk=input("Kirjuta igasugune palk ")
    palk=float(palk)
    for i in range(len(x)):
        if y[i]>palk: 
            print(f"{x[i]} saab suurem kui {palk}, ta saab {y[i]}")
        elif y[i]<palk: 
            print(f"{x[i]} saab väiksem kui {palk}, ta saab {y[i]}")
        else:
            print(f"{x[i]} saab täpselt {palk}")
def suurem_vaiksem(x:list,y:list): 
    asdasd=y.copy()
    for i in range(3):
        ind=asdasd.index(min(asdasd))
        print(f"{i+1} inimene - {x[ind]} saab väikse palk: {y[ind]}")
        asdasd.pop(ind)
        asdasd.insert(ind,max(y)+1)
    asdasd=y.copy()
    for i in range(3):
        ind=asdasd.index(max(asdasd))
        print(f"{i+1} inimene - {x[ind]} saab suur palk: {y[ind]}")
        asdasd.pop(ind)
        asdasd.insert(ind,min(y)+1)
def keskmine(x:list,y:list): 
    kesk=sum(y)/len(y)
    print(f"Keskmine palk on {kesk}")
    for i in range(len(x)):
        if y[i]>kesk:
            print(f"{x[i]} saab suurem kui keskmine palk, ta saab {y[i]}")
        elif y[i]==kesk:
            print(f"{x[i]} saab täpselt keskmine palk")
def tulumaks(x:list,y:list): 
    for i in range(0,len(y)):
        if y[i]<500:
            palk=y[i]
        elif 500>=y[i]<=1200:
            palk=(y[i]-500)-(y[i]-500)*0.2
        elif 1200>y[i]>=2099:
            palk=(500-(5/9)*(y[i]-1200))-(500-(5/9)*(y[i]-1200))*0.2
        else:
            palk=y[i]*0.2
        print(f"{x[i]} on maksuvaba palk {palk}")
def Inlet(x:list,y:list):
    for i in range(0,len(x)):
        x[i]=x[i].title()
        y[i]=round(y[i],1) 
        y[i]=int(y[i])
    return x,y
def upZP(x:list,y:list):
    vali=input("1, 2, 3:  ")
    if vali in ["3","1"]:
        aasta=input("Mitme aasta pärast soovite palka teada? ")
    if vali=="3":
        for o in range(0,len(x)):
            newy=y[o]
            for i in range(0,int(aasta)):
                newy+=newy*0.05
            print(f"{x[o]} palk {aasta} aasta pärast on {round(newy,2)} eurot")
    elif vali=="1":
        nimi=input("Keda soovite muudatustest teada? ")
        ind=x.index(nimi)
        newy=y[ind]
        for i in range(0,int(aasta)):
            newy+=newy*0.05
        print(f"{nimi} palk {aasta} aasta pärast on {round(newy,2)} eurot")
    else:
        arv=input("Mitut inimest me testime? ")
        for i in range(0,int(arv)): 
            nimi=input(f"Keda sa tahad kontrollida {i+1}? ")
            aasta=input("Mitme aasta pärast soovite palka teada? ")
            ind=x.index(nimi)
            newy=y[ind]
            for i in range(0,int(aasta)):
                newy+=newy*0.05
            print(f"{nimi} palk {aasta} aasta pärast on {round(newy,2)} eurot")
def rename(x:list):
    """Kirjeldus...
    :param list x: Inimeste järjend
    :rtype: list
    """
    for i in range(0,len(x),3):
        npi=input("Kirjuta uus nimi ")
        x.pop(i)
        x.insert(i,npi)
    return x

