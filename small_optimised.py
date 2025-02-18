"""
Program to find all unique prime numbers hidden within a given binary string, and less than a given integer number.
Optimised for smaller strings.
"""

from utilities import timer, is_prime
from numpy import fromiter, dtype, uint8
import cProfile
from math import isqrt, ceil, log2
from itertools import cycle


@timer
def sub_string_primes(string, maximum):
    result = set()

    length = len(string)
    len_cap = int(log2(2 ** ceil(log2(maximum)))) if maximum > 1 else None

    for i in range(length - 1):
        if string[i] != "1":
            continue

        for j in range(i + 1, min(len_cap + i, len(string))):
            if string[j] != '1':
                if j == i + 1:
                    result.add(2)
                continue

            # print(f"Index: {i}/{length - 1}:{j}/{min(len_cap + i, len(string)) - 1}, String: {string[i:j]}")

            sub_string = string[i:j + 1]
            if (num := int(sub_string, 2)) not in result:
                if (num <= maximum) if maximum else True:
                    if is_prime(num):
                        result.add(num)

    return result

@timer
def sub_string_primes2(string, maximum):
    result = set()

    length = len(string)
    len_cap = int(log2(2 ** ceil(log2(maximum)))) if maximum > 1 else None

    indexes = fromiter((i for i, x in enumerate(string) if x == "1"), dtype(uint8))

    print(indexes)

    for i in range(len(indexes) - 1):
        for j in range(i + 1, len(indexes) - (i + 1)):
            if j - i < len_cap:
                if is_prime((num := int(string[indexes[i]:indexes[j]], 2))) and num <= maximum:
                    result.add(num)

    return result


if __name__ == "__main__":
    bin_string, maximum = input("Enter a binary number and the maximum prime to find (0 for no limit): ").split(" ")

    # cProfile.run("sub_string_primes(bin_string, int(maximum))")

    # result, time = sub_string_primes2(bin_string, int(maximum))
    # print(f"Result: {result}\nElapsed time:q {time:.10f}")

    result, time = sub_string_primes2(bin_string, int(maximum))
    print(f"Result: {result}\nElapsed time:q {time:.10f}")

# 0  - 101011 99
# 1  - 0100001101001111 999999
# 2  - 01000011010011110100110101010000 999999
# 3  - 1111111111111111111111111111111111111111 999999
# 4  - 010000110100111101001101010100000011000100111000 999999999
# 5  - 01000011010011110100110101010000001100010011100000110001 123456789012
# 6  - 0100001101001111010011010101000000110001001110000011000100111001 123456789012345
# 7  - 010000110100111101001101010100000011000100111000001100010011100100100001 123456789012345678
# 8  - 01000011010011110100110101010000001100010011100000110001001110010010000101000001 1234567890123456789
# 9  - 0100001101001111010011010101000000110001001110000011000100111001001000010100000101000100 1234567890123456789
# 10 - 010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011 12345678901234567890