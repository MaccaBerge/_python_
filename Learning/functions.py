
# Keyword arguments

# 1
def Add(num1, num2):
    return num1 / num2

x = Add(num2=2, num1=5)

print(x)

# 2
def get_net_price(price, tax=0.07, discount=0.05):
    return price * (1 + tax - discount)

net_price = get_net_price(100, discount=0.06)

print(net_price)


# Recursive Functions - A recursive function is a function that calls itself until it doesn’t.

# 1
def count_down(start):
    print(start)

    next = start - 1
    if next > 0:
        count_down(next)


#count_down(3)

# 2
def sum(n):
    if n > 0:
        return n + sum(n-1)
    return 0


result = sum(100)
#print(result)


# Lambda Functions - Python lambda expressions allow you to define anonymous(no name) functions. The anonymous functions are useful when you need to use them once.

# 1
doubler = lambda x: x*2
#rint(doubler(16))


# Function Docstring - When the first line in the function body is a string, Python will interpret it as a docstring. And you can use the help() function to find the documentation of the add() function:
def add(a, b):
    """ Add two arguments
    Arguments:
        a: an integer
        b: an integer
    Returns:
        The sum of the two arguments
    """
    return a + b

#help(add)


# Function with variable length of arguments.

def func(*args):
    for i in args:
        print(i)

#func(1,2,3,4,5,6,7,8)


# Return multiple values from a function

def calculation(a, b):
    return a+b, a-b

print(calculation(50, 36))


