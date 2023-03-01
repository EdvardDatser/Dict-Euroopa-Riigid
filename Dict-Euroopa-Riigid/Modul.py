
sonastlik = {}
def Read(fail:dict):
    file=open(fail,"r", enconding ="utf-8-sig")
    for line in file:
        k v=line.strip().split('-')
        sonastlik[k.strip()] = v.strip()

print(sonastlik)

def Kirjuta(fail:dict):
    file=open(fail,"r", encoding= "utf-8-sig")
    for line in file:
        k,v=line.strip().split('-')
        sonastlik[k.strip()] = v.strip()
    riik=input("Lisa riik: ")
    pealinn=input("Tema pealinn: ")
    sonastlik.update({riik:pealinn})
    file.close()
    print(sonastlik)
    return sonastlik