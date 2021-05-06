# Belajar default argument value

#defaul name berfungsi memberikan pengisian default pada parameter
#sehingga pengisian parameter bersifat opsional
def say_hello(nama="aris"): #menggunakan sama dengan lalu ketik default value nya
    print(f"Hello {nama}!")

say_hello("karachi")
say_hello() #akan error jika tidak default argumen tidak dipasang, tetapi jika dipasang maka akan keluar hasil yg default

#bagaimana jika menggunakan lebih dari 1 parameter
def says_hello(nama_pertama="uchiha", nama_kedua=""): #ketika ada 2 parameter, jika ingin dipasang defaul argument, maka harus 22nya dipasang
    print(f"Hello {nama_pertama}-{nama_kedua}!")

says_hello("muhammad", "aris") #auto terpasang berurutan
says_hello(nama_kedua="shishui") #ketik parameter lalu sama dengan, maka akan terpasang di parameter tsb
says_hello(nama_kedua="uchiha", nama_pertama="madara") #pemasangan argumen parameter (ex: madara) boleh acak, ketika ada deklarasi parameternya
says_hello(nama_kedua="obito")