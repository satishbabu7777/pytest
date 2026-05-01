"""
main.py

This module contains utility functions for basic number operations:
- Check if a number is even
- Reverse a given integer number

Functions:
    is_even(number): Returns True if number is even, otherwise False
    reverse(number): Returns the reversed integer value
"""


def is_even(number: int) -> bool:
    # Check if input is not an integer
    if not isinstance(number, int):
        return False  # Invalid input, treat as not even

    # Return True if number is divisible by 2, otherwise False
    return number % 2 == 0


def reverse(number: int) -> int:
    # Stores the reversed number
    reversed_number = 0

    # Loop until all digits are processed
    while number > 0:
        # Extract last digit
        digit = number % 10

        # Build reversed number step by step
        reversed_number = reversed_number * 10 + digit

        # Remove last digit from original number
        number //= 10

    # Return final reversed number
    return reversed_number