def simple_gen():
    for x in range(3):
        yield x


# if you use the for loop it catches the exception and wont continue if there is no next!
for number in simple_gen():
    print(number)

# g is a iterator
g = simple_gen()

# You can also call next function to get the next value
# but then you need to take care of exception when there is not next!
print(next(g))
print(next(g))

# you can convert some objects to iterators
my_string = 'hello'

my_string_iter = iter(my_string)

print(next(my_string_iter))
