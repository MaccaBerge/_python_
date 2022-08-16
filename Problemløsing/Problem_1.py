'''
Create a function in Python that accepts two parameters. 
The first will be a list of numbers. 
The second parameter will be a string that can be one of the following values: asc, desc, and none.

If the second parameter is "asc," then the function should return a list with the numbers in ascending order. 
If it's "desc," then the list should be in descending order, and if it's "none," it should return the original list unaltered.
'''


def SortList(list, string):
    if string == 'abc':
        print(list)
        for index in range(len(list)):
            if list[len(list)-index-1] < list[len(list)-index-2]:
                list.insert(len(list)-index-2, list[len(list)-index-1])
                list.insert(len(list)-index-2, list[len(list)-index-1])
                del list[len(list)-index+1]
                del list[len(list)-index+1]
                print(list)

    elif string == 'cba':
        pass

    elif string == 'none':
        return list

SortList([4,3,2,1], 'abc')