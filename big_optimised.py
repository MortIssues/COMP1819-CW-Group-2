from utilities import timer, is_prime
from numpy import fromiter, dtype, uint8
from math import isqrt, ceil, log2
from multiprocessing import Pool, cpu_count
from time import time


def check_substring(sub_string, maximum):
    num = int(sub_string, 2)
    if (num <= maximum) if maximum > 0 else True:
        if is_prime(num):
            return num
    return None

@timer
def sub_string_primes(string, maximum):
    result = set()
    length = len(string)
    len_cap = 2 ** ceil(log2(maximum)) if maximum > 1 else length

    with Pool() as pool:
        tasks = []
        two_flag = False

        ss_start = time()
        for i in range(length - 1):
            if string[i] != "1":
                continue

            for j in range(i + 1, min(len_cap + i, len(string))):
                if string[j] != '1':
                    if not two_flag and j == i + 1:
                        two_flag = True
                    continue

                # print(f"Index: {i}/{length - 1}:{j}/{min(len_cap + i, len(string)) - 1}, String: {string[i:j]}")

                tasks.append((string[i:j + 1], maximum))
        ss_time = time() - ss_start

        p_start = time()
        result = set(filter(lambda x: x is not None, pool.starmap(check_substring, tasks)))
        if two_flag:
            result.add(2)
        p_time = time() - p_start

    return result, ss_time, p_time

@timer
def sub_string_primes2(string, maximum):
    result = set()
    length = len(string)
    len_cap = 2 ** ceil(log2(maximum)) if maximum > 1 else length

    with Pool() as pool:
        tasks = []
        two_flag = False

        ss_start = time()
        for i in range(length - 1):
            if string[i] != "1":
                continue

            for j in range(i + 1, min(len_cap + i, len(string))):
                if string[j] != '1':
                    if not two_flag and j == i + 1:
                        two_flag = True
                    continue

                # print(f"Index: {i}/{length - 1}:{j}/{min(len_cap + i, len(string)) - 1}, String: {string[i:j]}")

                tasks.append((string[i:j + 1], maximum))
        ss_time = time() - ss_start

        p_start = time()
        result = set(filter(lambda x: x is not None, pool.starmap(check_substring, tasks)))
        if two_flag:
            result.add(2)
        p_time = time() - p_start

    return result

@timer
def sub_string_primes3(string, maximum):
    setup_time = time()
    length = len(string)
    len_cap = 2 ** ceil(log2(maximum)) if maximum > 1 else length

    indexes = fromiter((i for i, x in enumerate(string) if x == "1"), dtype=uint8)

    tasks = []

    for i in range(len(indexes) - 1):
        for j in range(i + 1, len(indexes) - (i + 1)):
            if j - i < len_cap:
                tasks.append((string[indexes[i]:indexes[j]], maximum))
    setup_finish = time() - setup_time

    with Pool() as pool:
        return set(filter(lambda x: x is not None, pool.starmap(check_substring, tasks))), setup_finish

if __name__ == "__main__":
    bin_string, maximum = input("Enter a binary number and the maximum prime to find (0 for no limit): ").split(" ")
    (result, setup_time), total_time = sub_string_primes3(bin_string, int(maximum))

    print(f"Result: {result}\n"
          f"Total time: {total_time}\n"
          f"Total time: {setup_time}\n")