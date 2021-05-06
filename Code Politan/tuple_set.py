# Belajar Tuple
#hampir sama dengan list, tetapi tuple tidak bisa diubah datanya
#bersifat immutable(tidak bisa diubah)
pelanggan = ("aris", "lila", "selma", "mila", "adam")

print(pelanggan)

print(pelanggan[0])
#manfaat : mengembalikan data dari suatu proses dengan lebih dari satu data


#Belajar Set

#tipe data ini juga berfungsi menyimpan banyak data
#tetapi datatype set ini tidak bisa dilihat menurut index nya, karena posisinya selalu berubah ubah seiring waktu
#data yg dimasukan unik/tidak bisa ganda(sama)
pelanggan = {"aris", "lilis", "selma", "linlin"}
print(pelanggan)

pelanggan.add("mashashi") #cara menambah data di tipe data set
pelanggan.add("kishimoto")
print(pelanggan)

pelanggan.remove("selma") #cara menghapus data di tipe data set
print(pelanggan)

#print(pelanggan[1]) -> dia akan error karena >> datatype set tidak berurut 