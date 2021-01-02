class Person:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return f"My name is: {self.name} and my code is: {self.name}"

    def __len__(self):
        return 20

    def __del__(self):
        print('The object is delete!')


b = Person('Mehran', 123)

# Print function automatically calls the print function
print(b)

# len function calls __len__ function
print(len(b))

# del command delete the object or variable firm the memory and also calls __del__ from the class if it is implemented
del b
