from collections import namedtuple

Dog = namedtuple('Dog', ['age', 'breed', 'name'])

sammy = Dog(age=5, breed='Husky', name='Sam')

print(sammy.age)

print(sammy.breed)

print(sammy.name)
