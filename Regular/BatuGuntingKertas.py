from random import randint

Glist = ["Gunting", "Batu", "Kertas"]

komputer = Glist[randint(0,2)]

pemain = False

while pemain == False:
    #Set pemain ke True
    pemain = input("Gunting, Batu, Kertas ? : ")
    if pemain == komputer:
        print("Seri!")
        pemain = False
    elif pemain == "Batu":
        if komputer == "Kertas":
            print("Kamu Kalah!", komputer, "membungkus", pemain)
            pemain = False
        else:
            print("Kamu Menang!", pemain, "menghancurkan", komputer)
            pemain = False
    elif pemain == "Kertas":
        if komputer == "Gunting":
            print("Kamu Kalah!", komputer, "memotong", pemain)
            pemain = False
        else:
            print("Kamu Menang!", pemain, "membungkus", komputer)
            pemain = False
    elif pemain == "Gunting":
        if komputer == "Batu":
            print("Kamu Kalah!", komputer, "menghancurkan", pemain)
            pemain = False
        else:
            print("Kamu Menang!", pemain, "momotong", komputer)
            pemain = False
    else:
        print("Pilihan yang kamu masukan salah...")
        pemain = True

print('Permainan Selesai')
komputer = Glist[randint(0,2)]