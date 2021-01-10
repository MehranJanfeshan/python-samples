# This is a traditional way to calculate how much time takes to run a function!

import time
from timeit import timeit


def func_one(n):
    return [str(num) for num in range(n)]


def func_two(n):
    return list(map(str, range(n)))


start_time = time.time()

result = func_two(1000000)

end_time = time.time()

elapsed_time = end_time - start_time

print(elapsed_time)
