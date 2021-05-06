print("Pelajaran boolean")

menikah = False # "F" nya harus huruf besar
jomblo = True # begitupun denga "T" nya

print(menikah)
print(jomblo)
print("")

print("===Logic Operator===")

#operasi and (dan)
print(True and True) #hasilnya true
print(True and False) #jika ada mix false, maka hasilnya akan false
print(False and True) #ini juga sama
print(False and False) #ini juga sama
print("")

#operasi or (atau)
print(True or True) #hasilnya akan true
print(True or False) #berupa pemilihan ke jalan yg benar
print(False or True) # juga sama
print(False or False) # sudah pasti false, karna gada yg bener

print("===OPERASI PERBANDINGAN===")

#       >       lebih dari
#       <       kurang dari
#       >=      lebih dari sama dengan
#       <=      kurang dari sama dengan
#       ==      sama dengan         -> bisa utk perbandingan teks
#       !=      bukan sama dengan   -> bisa juga perbandingan str

print(1<=1) #hasilnya akan boolean
print(20>20.1)

print("gokuze" == "gokuze") # karna str nya sama, maka true
print("zhen" != "bokuno") # karna str-nya beda dan dgn !=, maka true
print("sasuke" == "shukaku") #akan false, karena str nya tidak sama
print("kaguya" != "kaguya") #akan false, karena memang sama dgn perbandingan tidak sama

print("")
v = "mazaya"
print("mazaya" == v) #true karena yg diambil adalah panggilan variabel "v"