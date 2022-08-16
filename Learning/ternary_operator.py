import random

'''
# First example
age = input('Enter your age\n\n>>> ')

ticket_price = 20 if int(age) >= 18 else 5

print(f'\nThe ticket will cost ${ticket_price}')
'''

# Second example
def Multiply(num1, num2):
    return num1 * num2

ran_num = Multiply(random.randint(1, 10), random.randint(1, 10))

answer = True if ran_num >= 50 else False

print(ran_num)
print(f'answer = {answer}')



