

def Calculator(int_1, operator, int_2):
    if operator == '+':
        return int_1 + int_2
    elif operator == '-':
        return int_1 - int_2
    elif operator == '/':
        return int_1 / int_2
    else:
        return 'Ikke gyldig operator!'


print(Calculator(5, '+', 83))