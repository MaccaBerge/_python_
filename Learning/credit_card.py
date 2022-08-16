
creditCardNumber = '4569971048837683'

def hideNumber(creditCardNumber):
    numberLen = len(creditCardNumber)
    for i in range(numberLen):
        if i % 4 == 0:
            print(' ', end = '')
        if numberLen - i > 4:
            print('*', end = '')
        else:
            print(creditCardNumber[i], end = '')
        

hideNumber(creditCardNumber)