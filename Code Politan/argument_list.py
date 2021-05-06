#Belajar Argument List
'''
def jumlahkan(satu, dua, tiga=0, empat=0): #tiga & empat yaitu default
    total = satu + dua + tiga + empat
    print(f"Total {[satu, dua, tiga, empat]} = {total}")

jumlahkan(10,10,10,10)
jumlahkan(8,8) #sehingga jika tidak memasukkan tiga & empat maka tidak error karena parameternya sudah default

#Bagaimana supaya kita tidak susah" menambah seperti itu, jika data yg ingin dimasukkan sangat banyak
#Yaitu dengan Argument List

def jumlahkan(x, *list_angka): #jika ingin menambah parameter maka diletakkan di awal (sebelum argumen list)
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"total {list_angka} = {total}")

jumlahkan(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) #angka 1 masuknya ke parameter x, sehingga yg dijumlahkan 2 - 5
'''

#Belajar Method return value
def jumlahkan(*list_angka): 
    total = 0
    for angka in list_angka:
        total = total + angka
    return (list_angka, total) #untuk mengembalikan list angka maka gunakan tuple

list_angka, total = jumlahkan(10, 10, 10) #memanggilnya pun mudah, hanya batasi antar variabel menggunakan koma

#Mengambil data total?
print(f"Total {list_angka} = {total}")