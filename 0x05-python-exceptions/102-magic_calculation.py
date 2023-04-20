#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0  # Initialize result to 0

    for i in range(1, 4):  # Loop from 1 to 3
        try:
            if i > a:
                # Raise an exception if i is greater than a
                raise Exception('Too far')
            # Perform the calculation and update the result
            result += (a ** b) / i
        except ValueError:
            pass  # Ignore any exceptions

    result += a + b  # Add a and b to the result

    return result  # Return the final result
