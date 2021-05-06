print("===exam type data===")

#ada 4 tipe data, yaitu int, float, str, and float
 
#type data int
ini = 9
print("data :", ini, "bertipe :", type(ini)) #cara cek nya

#cara mengubah type data
itu = str(ini) #mengubah variabel itu yg bertipe int menjadi tipe str,
print("data =", itu, "bertipe :", type(itu)) #variabel_name nya pun has changed

#mengubah yg sudah diubah
anu = float(itu)
print("data =", anu, "bertipe :", type(anu))

# lanjut ke boolean
ono = bool(anu)
print("data =", ono, "bertipe :", type(ono))

print("EXAM INPUT")

print("silahkan masukkan nama anda")
nama = str(input())
print("selamat datang", nama, "semoga harimu bahagia")

#mini kalkulator
print("input first number :")
a = int( input() )
print("input second number :")
b = int( input() )

hasil = a*b
print(f"{a} * {b} = {hasil}")

print("input first number :")
num1 = float(input())
print("input second number :")
num2 = float(input())
result = num1 + num2
print(f"{num1} + {num2} = {result}")