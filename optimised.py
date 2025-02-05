def int_sub_string(string):
    """ Function to search a binary string and seperate it into smaller, distinct sections.
    :param string: String to be subdivided.
    :return: Separated sections.
    :rtype: list of integers.
    """

    result = []

    for i in range(length := len(string)):
        for j in range(i + 1, length):
            result.append(int(string[i:j], 2))

    return list(dict.fromkeys(result))

def is_prime(num):
    """ Function to check if a number is a prime number.
    :param num: The number to be checked.
    :return: True or False depending on if the number is prime.
    :rtype: bool
    """

    for i in range(2, num ** 0.5):
        if num % i == 0:
            return False
    return True

def sub_string_primes(string, maximum):
    sub_strings = int_sub_string(string)
    return list(filter(is_prime, filter(lambda x: x < maximum, sub_strings) if maximum > 0 else sub_strings))


if __name__ == "__main__":
    bin_string, maximum = input("Enter a binary number and the maximum prime to find (0 for no limit): ").split()

    print(sub_string_primes(bin_string, int(maximum)))