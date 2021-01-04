my_list = [1, 2, 3]

# Adding multiple items to the list
my_list.extend([4, 6, 7])

# Adding one item to the list
my_list.append(12)

# get the size of list
print(len(my_list))

# get size of list
print(len(my_list))

# slicing and indexing work same as array!
print(my_list[0])

# concatenating two lists
my_list2 = [4, 5, 6]
print(my_list + my_list2)

# Update the list items
my_list[0] = 100
print(my_list)

# Append an item to the list
my_list.append(345)
print(my_list)

# Removing the last item from the list
print(my_list.pop())
print(my_list)

# sorting list - This changes the list and it does not return back anything!
my_list3 = ['a', 'n', 'c', 'f']
my_list4 = [5, 1, 4, 0, 3]
my_list3.sort()
my_list4.sort()
print(my_list3)
print(my_list4)

# Reverse method - This changes the list and it does not return back anything!
my_list3.reverse()
my_list4.reverse()
print(my_list3)
print(my_list4)
