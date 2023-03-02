from Modul import *


sonastik={}
riik_pealinn = {}
pealinn_riik ={}

while True:
    print(riik_pealinn)
    menu=int(input("Начальный словарь - 1\nНайти страну/столицу - 2\nДобавить в словарь - 3\nИсправить в словаре - 4\nЗакрыть - 0\n5Игра\n"))
    if menu == 0:
        break
    elif menu == 1:
        file("riigid_pealinnad.txt", sonastik, riik_pealinn, pealinn_riik)
    elif menu == 2:
        riigid_pealinn(riik_pealinn, pealinn_riik)
    elif menu == 3:
        file_add(riik_pealinn, pealinn_riik)
    elif menu == 4:
        file_change(riik_pealinn, pealinn_riik)
    elif menu == 5:
        game(riik_pealinn, pealinn_riik)