print("Nama : Muhammad Aris Septanugroho")
print("Kelas : X SIJA 1")

print('''Pilihan :
1. Operator Logika Not
2. Operator Logika And
3. Operator Logika Or''')

pilihan = int(input("masukkan angka pilihan :"))
print(pilihan)

if pilihan == 1:
    print("===Operasi Logika Not")

    a = int(input("input first number :"))
    b = int(input("input second number :"))

    print(not a<b)
    print(not a<=b)
    print(not a>b)
    print(not a>=b) 
    print(not a != b )

elif pilihan == 2:
    print("===Operasi Logika And")

    a = int(input("input first number :"))
    b = int(input("input second number :"))

    print(a<b and a>b)
    print(a<=b and a>=b)
    print(a==b and a!=b)
    print(a==b and a==b)


elif pilihan == 3:
    print("===Operasi Logika Or")

    a = int(input("input first number :"))
    b = int(input("input second number :"))

    print(a<b or a>b)
    print(a<=b or a>=b)
    print(a==b or a!=b)
    print(a==b or a==b)

else:
    print("Pilihan tidak tersedia")























