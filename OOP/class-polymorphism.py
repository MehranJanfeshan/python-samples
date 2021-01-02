class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + 'Says Woof!'


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + 'Says meow!'


niko = Dog('Niko')
felix = Cat('Felix')

# Dog and Cat class have a function with a same name but different functionality
for pet in [niko, felix]:
    print(type(pet))
    print((pet.speak()))
