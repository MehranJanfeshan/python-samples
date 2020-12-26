# Dictionaries are not in order so, if you iterate over them you may not get them in order
my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)

# get value for the key
print(my_dict['key1'])

# dictionary is very flexible and can hold list, or another dictionary
my_dict2 = {'key1': [1, 3, 4, 5], 'key2': {'key1': 'mehran', 'key2': 'auto'}}
print(my_dict2['key2']['key1'])

# Adding key value to the an existing dictionary
my_dict2['key3'] = 123
print(my_dict2)

# Overwrite a key value
my_dict2['key3'] = 456
print(my_dict2)

# get all the keys
print(my_dict.keys())

# get items in for of Tuples
print(my_dict.items())

# get values
print(my_dict.values())


