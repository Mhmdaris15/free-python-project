def hurufBergantian(inputString):
    init = inputString[0]
    output = 0
    for i in range(1, len(inputString)):
        if init == inputString[i]:
            output += 1
            init = inputString[i]
        else:
            init = inputString[i]

    return output

print(hurufBergantian('PCPCCPC'))