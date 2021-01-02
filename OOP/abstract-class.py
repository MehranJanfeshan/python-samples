# This class must be inherited and should not create any object from it!
class Animal:
    def __init__(self):
        print('Animal Created')

    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self)
        self.name = name

    def speak(self):
        return self.name + 'Says Woof!'


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self)
        self.name = name

    def speak(self):
        return self.name + 'Says meow!'


niko = Dog('Niko')
felix = Cat('Felix')

# Dog and Cat class have a function with a same name but different functionality
for pet in [niko, felix]:
    print(type(pet))
    print((pet.speak()))
