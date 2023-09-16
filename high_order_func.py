
# High order function: Function that takes a parameter and a second function to apply to the parameter.

def double(d):
    """
    Doubles the value of d
    """
    return d**2

def triple(t):
    """
    Triples the value of t
    """
    return t*3

def square_root(s):
    """
    Returns a square root of s
    """
    return s**0.5

def is_prime_n(n):
    """
    Returns is a prime number or not
    """
    if n <= 1:
        return False
    elif n == 2:
        return True
    # Even number greater than 2 are not a prime number.
    elif n % 2 == 0:
        return False
    # Checking for divisibility of odd numbers from 3 to square root of x
    # Starting from 1st odd number greater than 2, including int part of square root of n
    # With step-size of 2, that is escaping the next even after odd and so on.
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

def get_input_number():
    """
    Gets a user input and returns as output.
    """
    n = int(input("Enter a number: "))
    return n
def get_integer_n(msg):
    value_as_string = input(msg)
    while not value_as_string.isnumeric():
        print(f"Invalid Entry! Please enter a number only. You entered {value_as_string}")
        value_as_string = input(msg)
    return int(value_as_string)
def my_high_order_function(n, func):
    return func(n)
# Assigning the function with a user input to a variable.
# this way the user will have to enter only one output for several function call operations.
user_input = get_input_number()

r1 = my_high_order_function(user_input, double)
print(f"Double of {user_input} is {r1}")
r2 = my_high_order_function(user_input, triple)
r3 = my_high_order_function(user_input, square_root)
r4 = my_high_order_function(user_input,is_prime_n)




















