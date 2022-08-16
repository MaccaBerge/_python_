
def Palindrome_Check(string):
    if string == string[::-1]:
        return True
    else:
        return False

string = 'POP'
print(Palindrome_Check(string))