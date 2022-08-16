

def Repeat(string, duplicator):
    string_list = []
    for character in string:
        if character != ' ':
            for i in range(duplicator):
                string_list.append(character)
        else:
            string_list.append(' ')

    string = ''
    for i in string_list:
        string += i
    return string

duplicator = 2

print(Repeat('abc', duplicator))

