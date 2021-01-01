myString = 'My name is Mehran'
my_list = [letter for letter in myString]
print(my_list)

# perform an operation before adding item to the list
my_numbers = [num ** 2 for num in range(0, 11)]
print(my_numbers)

# adding if statement - adding only even numbers
my_numbers = [num for num in range(0, 11) if num % 2 == 0]
print(my_numbers)

# performing more complex arithmetic
celsius = [0, 10, 20, 34.5]
fahrenheit = [((9 / 2) * temp + 32) for temp in celsius]
