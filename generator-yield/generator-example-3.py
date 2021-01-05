import random


def gen_square(N):
    for i in range(N):
        yield i ** 2


for x in gen_square(10):
    print(x)


def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)


# basically for here helps us to go over the next item!
for num in rand_num(1, 10, 12):
    print(num)
