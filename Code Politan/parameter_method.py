# Belajar Method Parameter 
print("garuda")
# print -> termasuk method
# "garuda" -> termasuk parameter

def say_hello(name): #parameter = 1
    print(f"Hello {name}")

say_hello("susi susanti")

#menambah parameter hanya dengan koma
def says_hello(first_names, last_names):
    print(f"Hello {first_names} {last_names}")
#harus diberi 2 parameter, jika tidak maka error
says_hello("zhang", "xian") #karena di method def nya, berparameter 2