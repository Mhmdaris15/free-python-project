import numpy 

# x = int(input("Input n : "))
# y = input('Input an array : ')
# y = numpy.array(y.split(" ")).astype(int)
n = int(input())
arr = map(int, input().split())
z = []
for i in arr:
    if i in z:
        continue
    z.append(i)
z.sort(reverse=True)
print(z[1])