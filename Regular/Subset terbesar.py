def subsetTerbesar(inputList):
    amountList = len(inputList)
    result = []
    list_index = []
    biggest = 0
    for i in range(amountList):
        sums = 0
        list_index = range(i, amountList, 2)
        for j in list_index:
            sums += inputList[j]
        if sums > biggest:
            biggest = sums
        for k in range(amountList):
            sums = 0
            if (k != i + 1) and (k != i):
                sums = inputList[i] + inputList[k]
                if sums > biggest:
                    biggest = sums
    return biggest

