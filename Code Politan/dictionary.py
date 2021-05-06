# Belajar Tipe data Dictionary

customer = {"name":"aris", "age":18, "address":"Bogor"} 

#menggunakan tipe data set
#berbentuk "key dan value", key dianalogikan sebagai index yang bertipe string
#maka ketika dipanggil, tidak lagi menggunakan index int

print(customer["name"]) #seperti inilah index yg string 
print(customer["age"])
print(customer["address"])
print("==============")

'''for key in customer: #mengapa key? karena di loop-for yg keluar akan key, sedangkan valuenya tidak
    value = customer[key] #dibuat variabel value supaya mencantumkan valuenya index(key)
    print(f"{key}:{value}") #dengan begini key & value siap dipanggil'''

#print(customer.items()) #akan keluar hasil, dengan datatype tuple
#dalam 1 data ada key dan value, jika sudah di"tuple"kan, maka key berindex 0 dan value berindex 1

for key in customer.items():
    print(f"{key[0]}:{key[1]}") 

#datatype tuple bisa diekstrak menjadi beberapa variabel


#Menambah, mengubah, dan menghapus data

customer["company"] = "Zhuo Shi" #menambah data
customer["name"] = "Muhammad Aris" #mengubah data juga seperti ini

del customer["address"] #menghapus data

for key, value in customer.items(): #lebih simple lagi __ antarvariabel dipisah dengan koma
    print(f"{key}:{value}") 



#dalam membuat data customer seperti di atas
#dianjurkan menggunakan datatype dictionary
#karena utk mengakses datanya lebih simple dan mudah
#dibanding menggunakan list, karena kita tidak tahu index ke berapa