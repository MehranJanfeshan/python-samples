my_nums = [1, 2, 3, 4, 5]


def square(num):
    return num * 2


# using map function to execute square function for every item in the list
for item in map(square, my_nums):
    print(item)

# using builtin map and list to get the result from map in form of list!
my_list = list(map(square, my_nums))
print(my_list)
