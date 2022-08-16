
def Overlap(list_a, list_b):
    list_c = []
    for character in list_a:
        if character in list_b and not character in list_c:
            list_c.append(character)
    return list_c

a = [1,1,5,63,2,5,6,677,78,4,34,3]
b = [1,5,677, 4, 84, 35, 78, 3]

print(Overlap(a, b))
