#belajar if statement

hujan = 10
cerah = 10

if hujan < cerah :
    print("Turun hujan deras")

if hujan > cerah :
    print("hujan turun esok hari")

if hujan == cerah :
    print("angin tornado")

# if-else statement

menang = True

if menang : # karena datanya sudah bolean, ->
    print("Congratulations!") #maka tak perlu deklarasikan True lagi
else:  #setiap statement if harus diakhiri tanda ":"
    print("Silahkan coba lagi!")


# Belajar Elif

Pilihan_menu = input("masukkan pilihan :") #lebih simpel

if Pilihan_menu == "1":
    print("anda memilih pilihan 1")
elif Pilihan_menu == "2":
    print("anda memilih pilihan 2")
elif Pilihan_menu == "3" :
    print("anda memilih pilihan 3")
else :
    print("menu tidak tersedia") #pengeksekusian terbatas sampe sini

if Pilihan_menu == "x": #ini akan di eksekusi, terlepas dari yg atas
    print("anda memilih pilihan x") 