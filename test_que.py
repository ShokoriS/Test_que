# Function definitions
def add(*args):
    """Returns the sum of all input arguments."""
    return sum(args)


def multiply(*args):
    """Returns the product of all input arguments."""
    result = 1
    for num in args:
        result *= num
    return result


# Sample inputs
print(add(1, 3, 4, 5))          # Output: 13
print(add(1, 3))                # Output: 4
print(multiply(1, 2, 3, 4, 5))  # Output: 120
print(multiply(2, 3, 4))        # Output: 24
