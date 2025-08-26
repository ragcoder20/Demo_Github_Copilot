# Code to add 2 numbers in python
def add_numbers(a, b):
    return a + b

# code to check whether a number is prime or not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True