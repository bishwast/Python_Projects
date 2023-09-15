print("Sunil's Calculator App!")

"""
Defining set of functions that will implement the calculator operations below:
1. Addition
2. Subtraction
3. Multiplication
4. Division

- Functions will take 2 parameters and return another number. 
"""

def addition(x,y):
    """
    Adds two numbers from x and y variables.
    :returns x+y
    """
    return x+y

def subtraction(x,y):
    """
    Subtracts two numbers from x and y variables.
    :return: x-y
    """
    return x-y

def multiplication(x,y):
    """
    Multiplies numbers from variables x and y.
    :return: x*y
    """
    return x*y

def division(x,y):
    """
    Dividies x from y
    :param x:
    :param y:
    :return: quotient
    """
    return x/y

# Verification - Reject any input until user input is either y or n.
def check_if_the_user_has_finished():
    """
    Checks if the user wants to finish the operation or not.
    Performs verification on the users input.
    """
    # Fail closed approach - Always fail by closing down an application or the connection.
    ok_to_finish = True
    # Verify if the user has provided an acceptable input or not (y/n).
    user_input_accepted = False

    while not user_input_accepted:
        user_input = input("Do you want to continue? (y/n): ")
        if user_input == 'y':
            user_input_accepted = True
        elif user_input == 'n':
            user_input_accepted = False
        else:
            print("Invalid Entry! Please enter 'y' or 'n'.")
    # User is ok to finish / True if input is 'y' by default. If enters y python understands the boolean logic is False.
    return ok_to_finish



# Skeleton of the logic for calculator processing cycle.
# Boolean flag, to determine weather to terminate the main processing loop/not.
finished = False
# Main processing loop of the calculator.
while not finished:
    result = 0
    # Get the operation from the user.
    # Get the numbers from the user.
    # Select the operation.
    print(f"Result: {result}")
    # Determine if the user wants to continue/finished
    finished = check_if_the_user_has_finished()
print("Thank you for using the Calculator App!")

## Selecting the Operation






















