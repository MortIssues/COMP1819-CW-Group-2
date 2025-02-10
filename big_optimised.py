"""
Program to find all unique prime numbers hidden within a given binary string, and less than a given integer number.
Optimised for larger strings.
"""

from multiprocessing import Pool
from utilities import timer
import math
from functools import cache

@cache
def is_prime(num):
    """ Function to filter prime numbers from all substrings of a binary string only keeping numbers below a certain value.
    :param num: The number to be checked.
    :return: True or False depending on if the number is prime.
    :rtype: Bool
    """

    if num < 2:
        return False

    if num == 2:
        return True

    for i in range(3, math.isqrt(num) + 1, 2):
        if num % i == 0:
            return False

    return True

def filter_substrings(start, string, maximum):
    """ Function to filter substrings from a given index.
    :param start: The starting index.
    :param string: The string to be filtered.
    :param maximum: The maximum value to keep.
    :return: List of filtered numbers.
    :rtype: List[int]
    """

    results = set()
    current_value = 0

    for end in range(start, len(string)):
        current_value = (current_value << 1) | int(string[end])
        if string[end] == "0":
            continue

        if maximum > 0 and current_value > maximum:
            break

        if is_prime(current_value):
            results.add(current_value)

    return results

@timer
def sub_string_primes(string, maximum):
    """ Function to find prime numbers from all substrings of a binary string only keeping numbers below a certain value.
    :param string: The string to be filtered.
    :param maximum: The maximum value to keep.
    :return: List of filtered numbers.
    :rtype: List[int]
    """
    length = len(string)

    with Pool() as pool:
        results = pool.starmap(
            filter_substrings,
            [(start, string, maximum) for start in range(length)]
        )

    unique_primes = set()
    for result in results:
        unique_primes.update(result)

    return list(unique_primes)

if __name__ == "__main__":
    bin_string, maximum = input("Enter a binary number and the maximum prime to find (0 for no limit): ").split(" ")

    result, time = sub_string_primes(bin_string, int(maximum))
    print(f"Result: {result}\nElapsed time: {time:.10f}")
