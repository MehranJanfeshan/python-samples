# Read more about Python Quantifiers and Identifiers

import re

text = 'May phone number is 408-555-1234'

phone1 = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)

phone2 = re.search(r'\d*-\d*-\d*', text)

phone3 = re.search(r'\d{3}-\d{3}-\d{4}', text)

# You can group patterns and also you can still get them individually
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
phone4 = re.search(phone_pattern, text)

print(phone1)
print(phone2)
print(phone3)
print(phone4.group())

# start from index 1
# You can use this approach to extract part of the pattern!
print(phone4.group(1))
print(phone4.group(2))
print(phone4.group(3))
