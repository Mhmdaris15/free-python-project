import math
import os
import random
import re
import sys

# fptr = open(os.environ['OUTPUT_PATH'], 'w')

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

n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)
