class Dog:
    # Class attribute
    species = 'mammal'

    def __init__(self, my_breed, name, spot):
        # Object attribute
        self.breed = my_breed
        self.name = name
        self.spot = spot

    def bark(self):
        print(f'Woof! My name is {self.name}')


my_sample = Dog(my_breed='Lab', name='Johny', spot=False)
print(my_sample.breed)
print(my_sample.name)
print(my_sample.spot)
print(my_sample.species)
# You do not need to pass self as self refers to the object
my_sample.bark()
