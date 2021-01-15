x = [1, 2, 3]

# append add the list as an item
x.append([4, 5])
print(x)

# extend add each item as a separate item to the list
x.extend([4, 5])
print(x)

# Add an item to the specific index
x.insert(2, 'insert')
print(x)

# Remove an item from the list - the first occurrence
x.remove('insert')
