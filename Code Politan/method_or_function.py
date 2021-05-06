# Belajar Method atau Function
# Berguna memanggil beberapa kode, supaya tidak diketik ulang dan lebih simple

nama = []

def print_nama(): #deklarasikan dulu di awal. kode yg dibawah akan dipanggil dengan function
    print("=================") #jadi tidak perlu mengetiknya ulang banyak"
    for data in nama:
        print(data)

nama.append("mistuki")
print_nama() #berguna memanggil si function (print_nama)

nama.append("sakura")
print_nama()

nama.append("olya")
print_nama()

nama.append("yulya")
print_nama()