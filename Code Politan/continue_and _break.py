#continue dan break bisa digunakan di For-Loop dan While-Loop

#Belajar Continue --> Men-skip proses looping sehingga melanjutkan looping selanjutnya

#definisi menurut aris --> digunakan utk menolak data range

for i in range(1,10):
    if (i) % 2 == 1: #artinya ganjil
        continue #statment TRUE di atas akan dipentalkan dan tidak melanjutkan eksekusi
    print(i) #dan jika false, maka akan melewati continue dan singgah disini
#MAKA HASILNYA AKAN BIL. GENAP

for io in range(1,10):
    if (io) % 2 == 0: #artinya genap
        continue #statment TRUE di atas akan dipentalkan dan tidak melanjutkan eksekusi
    print(io) #dan jika false, maka akan melewati continue dan singgah disini
#MAKA HASILNYA AKAN BIL. GANJIL

print("====BREAK====")
#Belajar Break --> menstop looping nya sehingga tidak dilanjutkan lagi

for io in range(1, 100): #meski sampe 1000 jika sudah sampe batas break maka akan di stop
    if io % 45 == 0:
        break
    print(io)

#Penerapan pada while loop
while True:
    data = input("Masukkan pengulangan :")
    if data == "x" : #data akan looping terus hingga data yg diinput bernilai x
        break  #while loop menjadi lebih simple, tidak perlu menambah variabel di awal, cuma bikin Statement True setelah "while"
    print(data)