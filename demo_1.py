# Code to add 2 numbers in python
def add_numbers(a, b):
    return a + b

# code to check whether a number is prime or not
def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

    // Function to calculate compound interest with principal, rate, time, and compounding frequency
def calculate_compound_interest(principal, rate, time, frequency):
    """
    Calculate compound interest.

    Args:
        principal (float): The initial amount of money.
        rate (float): The annual interest rate (as a decimal).
        time (float): The time the money is invested for (in years).
        frequency (int): The number of times that interest is compounded per year.

    Returns:
        float: The amount of money accumulated after n years, including interest.
    """
    amount = principal * (1 + rate / frequency) ** (frequency * time)
    return amount

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    Args:
        principal (float): The initial amount of money.
        rate (float): The annual interest rate (as a decimal).
        time (float): The time the money is invested for (in years).

    Returns:
        float: The amount of interest earned.
    """
    return principal * rate * time