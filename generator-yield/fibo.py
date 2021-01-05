# No memory efficient
def gen_fibon(n):
    a = 1
    b = 1
    output = []
    for i in range(n):
        output.append(a)
        a, b, = b, a + b

    return output


# Memory efficient
def gen_fibon_2(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b, = b, a + b


for number in gen_fibon(50):
    print(number)
