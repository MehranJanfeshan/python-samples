# iterate over list
my_iterable = [1, 2, 3]
for num in my_iterable:
    print(num)

# iterate over string
my_string = "My name is mehran"
for char in my_string:
    print(char)

# iterate over tuple
my_tup = (1, 2, 3)
for item in my_tup:
    print(item)

# iterate without defining the temp variable
for _ in my_tup:
    print('Cool!')

# iterate over list of tuples - unpacking tuple
my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

for (a, b) in my_list:
    print(a)
    print(b)

# iterate over dictionary of tuples
my_dict = {'k1': 1, 'k2': 2, 'k3': 3}

for (key, value) in my_dict.items():
    print(key)
    print(value)

for value in my_dict.values():
    print(value)

for key in my_dict.keys():
    print(key)
