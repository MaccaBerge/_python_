
def Divisor(number):
    rangeList = list(range(1, number+1))
    divisorList = []

    for num in rangeList:
        if number % num == 0:
            divisorList.append(num)
    
    return divisorList

print(Divisor(30))