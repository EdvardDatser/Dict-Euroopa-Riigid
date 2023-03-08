from Modul import *


sonastik={}
riik_pealinn = {}
pealinn_riik ={}

while True:
    print(riik_pealinn)
    menu=int(input("Sõnaraamat - 1\nLeia riik/pealinn - 2\nLisa sõnaraamatusse - 3\nParanda sõnaraamatus - 4\nMäng - 5\nSulgemine - 0\n"))
    if menu == 0:
        break
    elif menu == 1:
        loe_fail("riigid_pealinnad.txt", sonastik, riik_pealinn, pealinn_riik)
    elif menu == 2:
        riigid_pealinn(riik_pealinn, pealinn_riik)
    elif menu == 3:
        Lisamine(riik_pealinn, pealinn_riik)
    elif menu == 4:
        Muuda(riik_pealinn, pealinn_riik)
    elif menu == 5:
        Teadmistekontroll(riik_pealinn, pealinn_riik)