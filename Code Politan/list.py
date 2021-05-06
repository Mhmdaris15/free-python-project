#belajar list

#jika kita ingin membuat banyak variabel, seperti inii
name1 = "sukiman"
name2 = "sukomo"
name3 = "sugiono"
#kita bisa menggunakan tipe data LIST
#kita akan lelah mengetik variabelnya satu", dan syntax akan menjadi sangat panjang
#oleh karnanya kita bisa menggunakan type data list ini

name = ["sukiman", "sukomo", "sugiono"]
name.append("hinata") #jika ingin menambah suatu data
name.append("naruto") #kita bisa gunakan format namavariabel.append
print(name)

#jika ingin mengecek data nya, kita bisa menggunakan index
#index dimulai dari 0

print(name[0]) #index menggunakan tanda [] lalu di dalamnya terdapat urutan ke sekian
print(name[1]) #index dimulai dari 0
print(name[2]) #misal kita mau cek data ke 7 yg kita tulis,
print(name[3]) #maka indexnya 6
print(name[4])

#jika kita ingin menghapus salah satu data, bisa menggunakan .remove
#jika kita menghapus salah satu data, maka index data setelahnya akan bergeser ke belakang
#berhati hatilah dalam menghapus data list

name.remove(name[0])
print(name)
print(name[0]) #ini akan menjadi sukomo, karena sukiman terhapus
print(name[1]) #ini juga bergeser dari sesudahnya

# Mengubah data List
name[2] = "sakura" #mengubah hinata -> menjadi sakura