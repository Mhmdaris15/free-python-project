#Belajar For Loop

pelanggan = ["satria", "deja", "hiro", "aris", "billy"]
pelanggan.append("tyas")
pelanggan.append("milla")

# mengakses semua nama pelanggan 
print(pelanggan[0])
print(pelanggan[1]) #menggunakan cara ini sungguhlah ribet
print(pelanggan[2]) #jika data mencapai ribuan
print(pelanggan[3]) #maka kita harus mengulang statement tsb ribuan kali
print(pelanggan[4]) #maka ada cara yg lebih simple
 
# mengakses data list dengan lebih SIMPLE
for nama in pelanggan:   #artinya -> memasukkan semua v pelanggan, ke dalam "nama"
    print(f"nama pelanggan = {nama}") #perintah ini akan terus diulang oleh for
    print("==================")#yang ada di bawah for akan diulang hingga selesai
