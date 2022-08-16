
def Xs_Os(string):
    x = 0
    o = 0
    if 'x' in string or 'o' in string:
        for letter in string:
            if letter == 'x':
                x += 1
            if letter == 'o':
                o += 1
        if x == o:
            return True
        
        return False

    return True

string = 'lhkhktkjkh'
print(Xs_Os(string))