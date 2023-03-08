from random import *

def loe_fail(f: str, s: dict, r: dict, p: dict):
    file=open(f, "r")
    for line in file:
        k, v=line.strip().split("-")
        s[k.strip()] = v.strip()
        r[k]=v
        p[v]=k
    file.close()
    return s, r, p

def riigid_pealinn(r:dict, p:dict):
    ans=int(input("Riik - 1, Pealinn - 2\n"))
    if ans == 1:
        riik = str(input("Riigi nimi.\n"))
        print(r[f"{riik}"])
    elif ans == 2:
        pealinn = str(input("Peallinna nimi.\n"))
        print(p[f"{pealinn}"])
    return r, p

def Lisamine(r:dict, p:dict):
        riik=input("Kirjutage Riik: ")
        pealinn=input("Kirjutage Pealinn: ")
        r.update({riik:pealinn})
        p.update({pealinn:riik})
        return r, p

def Muuda(r:dict, p:dict):
        riik = str(input("Sisesta riik, mida soovid parandada: "))
        pealinn = str(input("Sisesta pealinn, mida soovid parandada: "))
        r.pop(riik)
        p.pop(pealinn)
        riik2 = str(input("Sisetage uus riik: "))
        pealinn2 = str(input("Sisetage uss peallinn: "))
        r.update({riik2: pealinn2})
        p.update({pealinn2: riik2})
        return r, p

def Teadmistekontroll(r:dict, p:dict):
    riik=list(r.keys())
    pealinn=list(p.values())
    ko=0
    try:
        n = int(input("Kui palju küsimusi soovite?\n"))
    except:
        print(TypeError)

    k = int(input("Soovite nimetada pealinnu <1> või riike <2> ?"))
    for i in range(0,n):
        if k==1:
            rand=choice(riik)
            ind=riik.index(rand)
            print(pealinn[ind])
            sona=input("Sisesta: ")
            if sona in riik[ind]:
                print("Õige")
                ko+=1
            else:
                print("Vale")
        elif k ==2:
            rand=choice(pealinn)
            ind=pealinn.index(rand)
            print(riik[ind])
            sona = input("Sisesta: ")
            if sona in pealinn[ind]:
                print("Õige")
                ko+=1
            else:
                print("Vale")
    percent = round(ko / n * 100) 
    print(percent, "%")
