print('''Nama  : Muhammad Aris Septanugroho
Kelas : X SIJA \n ''')

a = int(input("Input 0 if you done : "))
c = []

while a != 0 :
    if a != 0 :
        b = a**2
        c.append(b)
        a = int(input("Input 0 if you done : "))
        continue
    else:
        break
print(c)
