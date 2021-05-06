print("====PENJUMLAHAN TYPE STRING====")
# belajar input number 

print("angka pertama :")
a = input()

print("angka kedua :")
b = input()

hasil = a + b
print(f"{a} + {b} = {hasil}") #hasilnya akan menggabungkan,
#                                karena type data string

print("====PENJUMLAHAN INTEGER====")
#supaya menjadi int maka harus dideklarasikan terlebih dahulu

print("angka pertama :")
a = int ( input() ) #dideklarasikan sebelum 'input'

print("angka kedua :")
b = int ( input() )

hasil = a + b
print(f"{a} + {b} = {hasil}")

# belajar input user
print("===INPUT USER===")

#hasilnya pasti string
data = input("masukkan nama :")
print("data :", data, "bertipe :", type(data))

#jika ingin mengambil int, makaa
angka = int(input("masukkan angka :"))
print("data :", angka, "bertipe :", type(angka) )

#bagaimana dengan boolean?
biner = bool(int(input("masukkan nilai boolean :"))) #di int kan dlu
print("data :", biner, "bertipe :", type(biner)) #harus input angka
