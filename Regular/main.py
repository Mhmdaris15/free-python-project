# def reverseNum(x):
#     x = str(x)
#     if x == x[::-1]:
#         return int(x)

# c = [i for i in range(1,10001) if reverseNum(i) != None]

# def Harshad(a):
#     a = str(a)
#     d = [a[i] for i in range(len(a))]
#     e = 0
#     for i in d:
#         e += int(i)

#     if int(a) % e == 0 :
#         return int(a)

# for i in range(1,51):
#     if Harshad(i) != None:
#         print(i)


Nama = "Muhammad Aris Septanugroho"
Number = 1
while Number < 10:
    if Number % 2 == 0:
        Number += 1
        continue
    print(Number, Nama)
    Number += 1


for i in range(1,10):
    print(i*' * *')
    print('It\'s the second line of {}th loops'.format(i))