import numpy as np
from numpy.lib.function_base import append
# n_array = int(input('berapa array yang ingin kau input?'))

# array = []
# for i in range(n_array):
#     a = int(input(f'array ke {i+1}: \n'))
#     b = int(input('dan : ' ))    
#     array.append([a,b])
# print(array)

arr = np.arange(0,100,10)
arr_odd = []
arr_even = []

odd = [arr[i] for i in range(len(arr)) if i % 2 != 0]
even = [arr[i] for i in range(len(arr)) if i % 2 == 0 ]
print(even, '\n', odd)

# for i in range(len(arr)):
#     if i % 2 == 0:
#         arr_even.append(arr[i])
#     else: 
#         arr_odd.append(arr[i])

# sum_odd = 0
# sum_even = 0

# for i in zip(arr_even, arr_odd):
#     sum_odd += i[1]
#     sum_even += i[0]

# sum_odd /= len(arr_odd)
# sum_even /= len(arr_even)

# print(f"Rata-rata [0]: {sum_even} \nRata-rata [1] : {sum_odd}")