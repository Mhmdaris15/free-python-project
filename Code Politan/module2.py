# Belajar Module

#Berguna memanggil data dari file py lain

#misal ingin memanggil data dari file module.py


import module

hello = module.say_hello("Mehmet Arizi") #dideklarasikan first, yaitu nama filenya tanpa ekstensi
print(hello)

hasil = module.total(1, 3, 5, 7, 9, 11, 13, 15)
print(hasil) 

print("")

#jika ingin import hanya beberapa method/function nya saja

from module import say_hello
from module import total
#ketika dgn spesifikasi, maka kita tidak perlu lagi deklarasi file/modulenya
hello = say_hello("Mehmet Selam")
print(hello)

hasil = total(1, 3, 5, 7)
print(hasil) 


# Dalam Membuat Program Di Python
# Menggunakan banyak file Itu sudah tidak asing lagi
# Pecah menjadi beberapa file
# Sehingga kita mudah mengecek datanya
# Karena itulah fungsi import module ini ada