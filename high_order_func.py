
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

def get_input():
    """
    Gets a user input and returns as output.
    """
    n = (input("Enter anything: "))
    return n

def get_integer_n(msg):
    """
    Gets an integer from the user.
    :param msg: Asks for user input as a prompt
    :return: integer
    """
    value_as_string = input(msg)
    while not value_as_string.isnumeric(): # Exit this loop if the user input is numeric.
        print(f"Invalid Entry! Please enter a number only. You entered {value_as_string}")
        # Re-Prompt for user input
        value_as_string = input(msg)
    # Convert users valid input from string to integer.
    return int(value_as_string)

def is_integer(n):
    """Checks for integer value and returns T/F"""
    return isinstance(n, int)



def check_user_input(user_input):
    if user_input.isdigit():
         print(f"You entered: {user_input}, and it is a number")
         return True
    elif user_input.isnumeric():
        print(f"You entered: {user_input}, and it is a number")
        return True
    elif user_input.isalpha():
        print(f"You entered: {user_input}, it is a letter")
        return True
    else:
        return False, f"Invalid Input! Your input was: {user_input}, and it is not a letter, number or a digit."

def my_high_order_function(n, func):
    return func(n)

# Assigning the function with a user input to a variable.
# this way the user will have to enter only one output for several function call operations.
user_input = get_input()

if user_input.isdigit():
    # If user input is a digit, then prompt for a number and perform operations.
    user_input = int(user_input)
    print(f"You entered {user_input} and it is a number.")
    r1 = my_high_order_function(user_input, double)
    print(f"Double of {user_input} is {r1}")
    r2 = my_high_order_function(user_input, triple)
    print(f"Triple of {user_input} is {r2}")
    r3 = my_high_order_function(user_input, square_root)
    print(f"Square root of {user_input} is {r3}")
    r4 = my_high_order_function(user_input,is_prime_n)
    print(f"Is {user_input} a Prime Number? (True/False): {r4}")
    r5 = my_high_order_function(user_input, is_integer)
    print(f"Is {user_input} an Integer? (True/False): {r5}")

else:
    # If user_input is not a digit, call check_user_input function and perform.
    valid, message = check_user_input(user_input)
    if valid:
        print(message)
    else:
        print(message)



















