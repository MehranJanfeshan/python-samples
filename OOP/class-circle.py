class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def get_circumfrenece(self):
        return self.radius * self.pi * 2

    def get_circumfrenece_2(self):
        # You can use class name instead of self to refer to the class level properties
        return self.radius * Circle.pi * 2


my_circle = Circle()

print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumfrenece())
