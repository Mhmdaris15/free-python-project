# game tebak tebakan
""" Q = "Apa ibukota jerman"
Answer = 'Berlin'
correction = False
while correction == False:
    print(Q)
    answer = (input("masukkan Jawabanmu : ")).capitalize()
    if answer == Answer:
        correction = True
    else:
        print('salah coba lagi! \n')
        continue
    print('selamat kamu menang! \nIbu Kota Jerman adalah Berlin')
 """
# a = 'halo dunia!'
# a = a.capitalize()
# print(a)


# TO DO LIST PROGRAMM

to_do = []
kondisi = False
while kondisi == False:
    print("Apa yang akan anda lakukan hari ini?\n1. Add To-DO List\n2. Delete a TO-DO List")
    try:
        quest = int(input("Jawab : "))
    except ValueError:
        print("masukkan input bertipe data integer!\n")
        continue
    if quest == 1 :
        doing = input('I will doing : ... ')
        to_do.append(doing)
        for i in to_do:
            print(f"$ {i}")
        print(" ")
    elif quest == 2:
        n = int(input(f'Pilihan ke berapa yang ingin anda hapus?\n{to_do}\n:...'))
        try :
            del to_do[n-1]
            print(to_do)
        except IndexError or ValueError:
            print('pilihan tidak tersedia\n')
            continue
    else:
        kondisi = True
        print("Program Berakhir!")