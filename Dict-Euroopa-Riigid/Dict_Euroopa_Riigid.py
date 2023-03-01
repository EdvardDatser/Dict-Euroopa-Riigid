from Modul import *

sonastlik = {}
while True:
    menu=int(input("\n0-Exit\n1-Read\n2-Kirjuta\n"))
    if menu==0:
        break
    if menu==1:
        sonastlik=Read("riigid_pealinnad")
    elif menu==2:
        sonastlik=Kirjuta("riigid_pealinnad")
    