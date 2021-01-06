import math
from math import pi

value = 4.35

print(math.floor(value))

print(math.ceil(value))

# infinity
print(math.inf)

# null number
print(math.nan)

print(pi)

# round is not part of math module as it is very common
# when it comes to the .5 round always generate even number
print(round(4.5))

print(round(4.6))

print(round(5.5))

# log - define base - here base is 10
print(math.log(100, 10))

# base log
print(math.log(100))
