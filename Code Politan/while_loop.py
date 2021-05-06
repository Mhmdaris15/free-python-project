#Belajar while-loop 

data = ""

# pada while loop perintah diulang berdasarkan data boolean
# jika data true maka akan terus di eksekusi sampai data tsb false

while data != "x":
    print("masukkan perulangan") #kata ini akan di print karna sejak awal sudah True
    data = input("data :") #digunakan variabel supaya yg kita input auto masuk ke while data. dan akan diinput seterusnya sampai data yg kita input False


# review program for loop
banyak = int(input("berapa banyak data : ")) 

nama = []
tinggi_badan = []
berat_badan = []

for ii in range(0, banyak):
    print(f"data ke {ii}")
    data_nama = input("nama :")
    data_tinggi_badan = int(input("tinggi :"))
    data_berat_badan = int(input("berat :"))

    nama.append(data_nama)
    tinggi_badan.append(data_tinggi_badan)
    berat_badan.append(data_berat_badan)

print(nama)
print(tinggi_badan)
print(berat_badan)

for ii in range(0, len(nama)): #mengapa diawali 0, karena kita akan pakai index utk statement di bawahnya
    data_nama = nama[ii] #dibuat variabel supaya mudah di print
    data_tinggi_badan = tinggi_badan[ii] # maksud [ii] adalah tinggi_badan ke-berapa,
    data_berat_badan = berat_badan[ii] # menurut urutan range, karna ii berisi kumpulan angka (range) 
    print(f"{data_nama} memiliki tinggi {data_tinggi_badan} dan berat {data_berat_badan}")

#variabel yg memuat nama yg dipanggil berupa BUKAN LIST!!!