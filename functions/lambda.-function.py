my_nums = [1, 2, 3, 4, 5, 6]

# Define lambda function and use it with map
square = lambda num: num ** 2

print(list(map(square, my_nums)))

# Define lambda function directly within map function

print(list(map(lambda num: num * 2, my_nums)))
