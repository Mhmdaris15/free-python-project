var = [1,2,3]
# print([i for i in range(len(var), 0, -1)])
print(len(var))
print(list(enumerate(var, start=1)))

metr = [[1,2,3,4],[4,5,6,7],[7,8,9,10],[11,12,13,14]]
def diagonalDifference(arr):
    first = []
    for i, v in enumerate(arr):
        first.append(v[i])
    second = []
    for i, v in zip(range(len(arr), 0, -1), arr):
        second.append(v[i-1])
    x = 0
    y = 0
    for i in first:
        x += i
    for i in second:
        y += i
    return abs(x-y)

print(diagonalDifference(metr))
