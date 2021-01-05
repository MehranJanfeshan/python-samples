from collections import Counter

my_list = [1, 1, 1, 1, 2, 2, 2, 4, 4, 6, 6, 8]

print(Counter(my_list))

print(Counter('Python'))

# Counter the number of words in this sentence!
my_str = "How many times does each word show up in this sentence with a word"
print(Counter(my_str.split()))

# Returns most common items (most repeated) - sorter tuples
print(Counter(my_str.split()).most_common())

# Returns two most common words
print(Counter(my_str.split()).most_common(2))

