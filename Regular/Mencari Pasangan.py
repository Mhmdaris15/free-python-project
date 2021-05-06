
# lst = [1, 2, 3, 4, 6, 9]
# integ = 15
# result = []
# if len(lst) < 2:
#     raise ValueError
# for i in lst:
#     for j in lst:
#         if i + j == integ:
#             result.append([i, j])

# if len(result) != 0:
#     print(result)


# lst = [1, 2, 3, 4, 6, 9]
# integ = 15
# result = []
# if len(lst) < 2:
#     raise ValueError
# for i in range(len(lst)):
#     for j in range(len(lst)):
#         if i == j:
#             continue
#         elif lst[i] + lst[j] == integ:
#             result.append([lst[i], lst[j]])
            

# if len(result) != 0:
#     print(result)


def cariPasangan(lst, integ):
    result = []
    if len(lst) < 2:
        raise ValueError
    for i in lst:
        for j in lst:
            if (i + j == integ) and ([j,i] not in result):
                result.append([i, j])
    if len(result) != 0:
        return result

print(cariPasangan([1, 2, 3, 4, 5], 7))