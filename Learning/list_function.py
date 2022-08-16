

string = 'jgfh5957shiuhug57757575uishgisugh575uighuigh5'

def Func(string):
    numbers = []
    for i in string:
        try:
            i = int(i)
        
        except:
            continue
        
        else:
            numbers.append(i)
    return numbers

print(Func(string))