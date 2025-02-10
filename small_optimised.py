"""
Program to find all unique prime numbers hidden within a given binary string, and less than a given integer number.
Optimised for smaller strings.
"""

from utilities import timer
import numpy as np
import cProfile
import math


def is_prime(num):
    """ Function to check if a number is a prime number.
    :param num: The number to be checked.
    :return: True or False depending on if the number is prime.
    :rtype: bool
    """

    if num < 2:
        return False

    if num == 2:
        return True

    for i in range(3, math.isqrt(num) + 1, 2):
        if num % i == 0:
            return False

    return True

@timer
def sub_string_primes(string, maximum):
    """ Function to fina all prime substrings of a binary string.
    :param string: The binary string.
    :param maximum: The maximum value to include.
    :return: List of prime substrings.
    :rtype: List[int]
    """

    result = set()

    for i in range(length := len(string) + 1):
        for j in range(i + 1, length):
            sub_string = string[i:j]

            if (sub_string[-1] != "0"
                and (iss := int(sub_string, 2)) not in result
                and ((iss <= maximum) if maximum > 0 else True)
                and is_prime(iss)):

                result.add(iss)

    return result


if __name__ == "__main__":
    bin_string, maximum = input("Enter a binary number and the maximum prime to find (0 for no limit): ").split(" ")

    # cProfile.run("sub_string_primes(bin_string, int(maximum))")

    result, time = sub_string_primes(bin_string, int(maximum))
    print(f"Result: {result}\nElapsed time:q {time:.10f}")