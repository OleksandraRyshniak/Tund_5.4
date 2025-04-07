from multiprocessing import Value
p=[]
i=[]

def valik1(p:list, i:list):
    """Uute inimeste lisamine
    Funktsioon lisab nimed ja nende palgad.
    :param list palgad
    :param list inimesed
    :rtype: None
    """
    while True:
        try:
            kogus=int(input("Kui palju inimesi soovite lisada: "))
            break
        except ValueError:
            print("Kogus on arv!")
    for k in range(kogus):
        while True:
            try:
                nimi=input("Sisesta nimi: ")
                if nimi.isalpha():break
            except:
                print("Nimi peaks koosnema ainult tähtedest!")
        while True:
             try:
                palk=float(input("Sisesta tema palk: "))
                break
             except ValueError:
                print("Palk on arv!")
        p.append(palk)
        i.append(nimi)
        print("Inimene lisatud!")

def valik2(p:list, i:list):
    """Isiku eemaldamine nimekirjast
    Funktsioon eemaldab isiku ja tema palga nimekirjadest.
    :param list palgad
    :param list inimesed
    :rtype: None
    """
    while 1:
        try:
            nimi=str(input("Sisesta nimi: "))
            if nimi.isalpha():
                if nimi in i:
                    break
                else:
                    print("Nime ei ole nimekirjas!")
        except:
            print("Nimi peab koosnema tähtedest!")
    k=i.count(nimi)
    if k>0:
        for j in range(k):
            ind=i.index(nimi)
            i.pop(ind)
            i.pop(ind)
            print("Nimekirjast eemaldatud nimi")

def valik3(p:list, i:list):
    """Suurim palk
    Funktsioon näitab kõrgeimat palka ja seda, kes seda saab.
    :param list palgad
    :param list inimesed
    :rtype: None
    """
    suurim=max(p)
    print(f"Suurim palk on {suurim}")
    k=p.count(suurim)
    ind=p.index(suurim)
    for i in range(k):
        ind=p.index(suurim,ind)
        print(f"Saab kätte {i[ind]}")
        ind+=1

def valik4(p:list, i:list):
    """Väikseim palk
    Funktsioon näitab väikseimat palka ja seda, kes seda saab.
    :param list palgad
    :param list inimesed
    :rtype: None
    """
    väiksem=min(p)
    print(f"Väiksem palk on {väiksem}")
    k=p.count(väiksem)
    ind=p.index(väiksem)
    for i in range(k):
        ind=p.index(väiksem,ind)
        print(f"Saab kätte {i[ind]}")
        ind+=1

def valik5(p:list, i:list):
    """Korraldada palgad
    Funktsioon korraldab palgad kahanevas ja kasvavas järjekorras (kasutaja valib)
    :param list palgad
    :param list inimesed
    :rtype: None
    """
    while True:
        v=input("Vali märk: > (kasvav) või < (kahanev)")
        if v==">" or v=="<":
            for n in range(0, len(i)):
                for m in range(n, len(i)):
                    if eval (str(p[n])+v+str(p[m])):
                        p[n],p[m]=p[m],p[n]
                        i[n],i[m]=i[m],i[n]
            print(i, p)
        else:
            print("Valige ainult > või <")

def valik6(p:list, i:list):
    """Kes saab sama palka
    Funktsioon näitab, kes saab sama palka ja kui palju selliseid inimesi on
    :param list palgad
    :param list inimesed
    :rtype: None
    """
    hulk=set(p)
    print(hulk)
    for palk in hulk:
        k=p.count(palk)
        if k>1:
            print(f"Palk {palk}")
            ind=p.index(palk)
            for n in range (k):
                ind=p.index(palk, ind)
                print(f"Saab kätte {i[ind]}")
                ind+=1

def valik12(p:list, i:list):
    """Korraldage nimed
    Funktsioon järjestab nimed kasvavas või kahanevas järjekorras (kasutaja valib).
    :param list palgad
    :param list inimesed
    :rtype: None
    """
    while 1:
        try:
            v=int(input("Vali 1.'A-st Y-ni' või 2.'Z-st A-ni': "))
            break
        except:
            print("Valik on arv!")
    if v == 1:
        list_sort=sorted(i)
    elif v==2:
        list_sort=sorted(i,reverse=True)
    else:
        print(" ")
    for n in range(0,len(i)):
        print(list_sort[n])

def valik7(p:list, i:list):
    """Palga otsimine isiku nime järgi
    Funktsioon otsib palku kasutaja poolt sisestatud nime järgi.
    :param list palgad
    :param list inimesed
    :rtype: None
    """
    while True:
        try:
            nimi=input("Sisetsa nimi: ")
            if nimi.isalpha():
                break
        except:
            print("Nimi peaks koosnema tähtedest!")
    k=i.count(nimi)
    if k>0:
        for ind in range(len(i)):
            if i[ind]==nimi:
                print(i[ind], p[ind])

def valik11(p:list, i:list):
    """Kättesaadav palk
    Funktsioon arvutab palga ilma tulumaksuta
    :param list palgad
    :param list inimesed
    :rtype: None
    """
    tulu=0.20 #20%
    for n in range(0, len(p)):
        if p[n]>654:
           palk=p[n]*tulu
           print(f"{i[n]}:{p[n]-palk}")
        else:
            print(f"{i[n]}: {p[n]}")

def valik13(p:list, i:list):
    """Funktsioon otsib need, kes saavad keskmisest madalamat palka,
   ja eemaldab nad nimekirjast.
    :param list palgad
    :param list inimesed
    :rtype: None
    """
    summ=0
    kogus=len(p)
    for n in range(0,len(p)):
        summ+=p[n]
    keskmine=summ/kogus
    m=len(p)-1
    while m>=0:
        if p[m]<keskmine:
            i.pop(m)
            p.pop(m)
        m-=1
    for j in range(0,len(i)):
        print(f"{i[j]} : {p[j]}")

def valik14(p:list, i:list):
    """Nimekirjade redigeerimine
    Funktsioon redigeerib nimekirju nii, et inimeste nimekirjas on nimed suurtähtedega, palgad int-formaadis.
    :param list palgad
    :param list inimesed
    :rtype: None
    """
    palk=list(map(int,p))
    for n in range (0, len(i)):
        i[n].capitalize()
    for j in range (0, len(p)):
        print(f"{i[j]} : {palk[j]}")
