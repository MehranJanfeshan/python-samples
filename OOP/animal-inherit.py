class Animal:
    def __init__(self):
        print('Animal Created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')


# Dog class inherited Animal class
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')

    # overwrite the parent function
    def who_am_i(self):
        print('I am a dog')

    # Adding a new method!
    def bark(self):
        print('WOOF!')


myDog = Dog()
myDog.who_am_i()
myDog.bark()
