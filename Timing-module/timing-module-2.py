# timeit helps you to do the test on your function and checks its performance
import timeit

stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]

'''

timeit.timeit(stmt, setup, number=100000)

stmt_2 = '''
func_two(100)
'''

setup_2 = '''
def func_two(n):
    return list(map(str, range(n)))

'''

print(timeit.timeit(stmt, setup, number=100000))
print(timeit.timeit(stmt_2, setup_2, number=100000))
