# Belajar Range
'''
#range digunakan untuk menginput data yg berupa angka berurutan terhingga
nomor = [1,2,3,4,5,6,7,8,9,10] #supaya ga susah maka pake range
nomor = range(1, 11)#aturan range yaitu ditulis angka awal dan angka akhir + 1

for no in nomor:
    print(no)

for no in range(1,13): # cara yang lebih sering digunakan
    print(no)
    '''

number = range(1, 10001)
for i in number:
    print(i)

#CARA MENG COMPILE PYTHON
#   1. BUKA TERMINAL DAN KETIK
#   2. python -m py_compile range.py
#   3. masuk ke direktori __py.compile__ dengan --> cd __py.compile__
#   4. Run bytecode (hasil compile) dengan --> python range.compile.pyc