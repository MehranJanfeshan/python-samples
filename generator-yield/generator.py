# This is not memory efficient
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x ** 3)
    return result


# This is memory efficient as yields the items as arrives
def create_cubes_yield(n):
    for x in range(n):
        yield x ** 3


for x in create_cubes(10):
    print(x)

for x in create_cubes_yield(10):
    print(x)
