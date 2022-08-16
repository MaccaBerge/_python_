
'''Sorting a list'''
numbers = [4, 6, 2, 66, 232, 6, 3, 2, 1, 6, 78, 87, 77, 7, 5, 5, 56]

# Sort the list from right to left (alphabetically)
numbers.sort()
print(numbers)

# Sort the list from left to right (reverse)
numbers.sort(reverse=True)
print(numbers)


'''Using the Python List sort() method to sort a list of tuples'''

companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]


companies.sort(key=lambda company: company[2], reverse=True)

print(companies)


'''Key argument in sort-function'''

students = [('Chris', 15),
            ('Charles', 16),
            ('Anne', 13)]


students.sort(key=lambda student: student[0])

print(students)








