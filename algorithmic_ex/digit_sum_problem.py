"""
Problem: Given a set of digit find a sum of NN digit numbers where each digit belong to given
         set of digits.

Solution: Find the sum of N-Digit numbers where each digit belongs to a given set of digits.

Input: Set of digits = digit_set
       Number of digits in the number = N

Initializing Sum: total_sum = 0

Iterate N times: Generate N-Digit numbers one digit at a time.
                 For each position iterate through the digit_set.
                 Add the current digit to the sum.

Repeat for N-digit numbers: Iterate N times again for the desired number of N-Digit numbers needs to be summed.

Placing a digit in the appropriate place = 10^(N-1)
    Where, N Represents a number in a number of digit.
           (N-1) Represents the position of the digit within a number.
    Example, If N=2, means I am constructing a 2-digit number,
             (2-1 = 1) Indicating the rightmost position in a 2-digit number
"""

def sum_of_num_in_digit(digit_set, N, count):
    """
    :param digit_set: Set of digit
    :param N: Number in a given digit_set
    :param count: determines how many times the process of counting ie repeated
    :return: sum of digits in a N-number of digit
    """
    total_sum = 0

    for i in range(count):
        current_number =0
        for n in range(N):
            # Iterate through the digit_set and add them
            for d in digit_set:
                current_number += d * (10**(N-1))
        total_sum += current_number
    return total_sum


