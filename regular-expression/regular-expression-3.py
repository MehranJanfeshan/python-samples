# Read more about Python Quantifiers and Identifiers

import re

text = 'The cat is here!'

# You can use | as or to search for more than one item
result = re.search(r'cat|dog', text)
print(result.group())

# user wildcard . to include whatever words that contain the pattern
# the wildcard period represent the character and if you add more it looks for more character
# before the actual key!
result = re.findall(r'.at', 'The cat in the hat sat there!')
print(result)

# the wildcard period represent the character and if you add more it looks for more character
# before the actual key!

result = re.findall(r'...at', 'The cat in the hat sat there!')
print(result)

# Exclude digits from the string
phrase = 'There are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]+'
print(re.findall(pattern, phrase))

# Exclude punctuation and space from the phrase

phrase = 'This is a string! But it has punctuation. How can we remove it?'
pattern = r'[^!.? ]+'
result = re.findall(pattern, phrase)

# join the item of list
print(' '.join(result))
