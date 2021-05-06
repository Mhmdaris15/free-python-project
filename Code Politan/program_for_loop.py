#Membuat program menggunakan For-Loop, List, dan Range

banyak = int(input("berapa banyak data :"))

nama = []
umur = []
#for akan mengulang data list atau range
for i in range(0, banyak): #isi data i adalah angka dari 0 s/d angka "banyak")-> range
    print(f"data ke {i}") #print data ke i (karena isi dari i adalah kumpulan angka)
    input_nama = input("nama :") #dibuat variabel utk input supaya memudahkan add to list 
    input_umur = int(input("umur :"))

    nama.append(input_nama) #data yg diinput akan ditambah disini
    umur.append(input_umur) #karena itulah fungsi dibuat variabel

print(nama)
print(umur) # hasilnya akan (nama, nama, nama) & (umur, umur, umur)

#bisa juga menggunakan for in
for i in range(0, len(nama)): #len nya bisa juga umur, karena jumlahnya sama
    data_nama = nama[i]
    data_umur  = umur[i]
    print(f"{data_nama} berumur {data_umur} tahun")