from time import time
from matplotlib.pyplot import figure, show
from math import isqrt
from functools import cache

# @cache # This functions the same as @lru_cache(None)
def is_prime(num):
    """ Function to filter prime numbers from all substrings of a binary string only keeping numbers below a certain value.
    :param num: The number to be checked.
    :return: True or False depending on if the number is prime.
    :rtype: Bool
    """

    for i in range(3, isqrt(num) + 1, 2):
        if num % i == 0:
            return False

    return True

def timer(func):
    """ Decorator for timing the execution of a function.

    :param func: Function to be timed.
    :return: A wrapped function that executes the original function and prints the elapsed time.
    :rtype: function.
    """

    def wrapper(*args, **kwargs):
        """ Wrapper function for the timer.
        :param args: Arguments.
        :param kwargs: Keyword arguments.
        :return: A tuple containing the result of the function and the elapsed time.
        """

        start = time()
        result = func(*args, **kwargs)
        return result, time() - start
    return wrapper

def show_results(results):
    """ Plots the results provided in a 2D array format.
    :param results: 2D array with each interior array in the format [x, y].
    """

    fig = figure()
    x = []
    y = []
    for result in results:
        x.append(result[0])
        y.append(result[1])

    show()