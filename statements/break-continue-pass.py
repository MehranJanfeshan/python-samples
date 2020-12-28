# pass
x = [1, 2, 3]
for item in x:
    pass

# continue
myString = 'Mehran'

for letter in myString:
    if letter == 'e':
        continue
    print(letter)

# break in for
for letter in myString:
    if letter == 'e':
        break
    print(letter)

# break in while
x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
