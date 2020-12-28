# range
for num in range(10):
    print(num)

# range with step - step here is 2
for num in range(0, 10, 2):
    print(num)

# range and list - get the list of items in the list

my_list = list(range(0, 11, 2))
print(my_list)

# enumerate - gets back the tuples that has index and char
word = "python"
for item in enumerate(word):
    print(item)

for index, letter in enumerate(word):
    print(index)
    print(letter)

# zip function merge lists together as a tuple - it ignores whatever is extra!
my_list1 = [1, 2, 3]
my_list2 = ['a', 'b', 'c']

for item in zip(my_list1, my_list2):
    print(item)

print(list(zip(my_list1, my_list2)))

# in - checks if an item exists in the list, string, dictionary

print('x' in ['x', 'y', 'z'])
print('x' in 'xbox')
print('key3' in {'key1': 123})
# check in values of dictionary
print(123 in {'key1': 123}.values())


# min and max

my_list3 = [1, 2, 3, 4, 5]
print(min(my_list3))
print(max(my_list3))