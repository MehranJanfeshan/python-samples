import random

# get the random number between 0 to 100 - everytime you get different number
print(random.randint(0, 100))

# set the seed - this time you always same number unless you change the seed!
random.seed(11)

print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))

# choice function
my_list = (range(0, 20))

my_random = random.choice(my_list)
print(my_random)

# Sample With replacement - there is a chance you get same number twice
print(random.choices(population=my_list, k=10))

# Sample Without replacement - you get unique number
print(random.sample(population=my_list, k=10))

# shuffle list - this affect the list
my_list2 = [1, 2, 3, 4, 5, 99, 7, 8, 13, 20]
random.shuffle(my_list2)
print(my_list2)
