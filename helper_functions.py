import time
import matplotlib.pyplot as plt

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

        start = time.time()
        result = func(*args, **kwargs)
        return result, time.time() - start
    return wrapper

def show_results(results):
    """ Plots the results provided in a 2D array format.
    :param results: 2D array with each interior array in the format [x, y].
    """

    fig = plt.figure()
    x = []
    y = []
    for result in results:
        x.append(result[0])
        y.append(result[1])

    plt.show()