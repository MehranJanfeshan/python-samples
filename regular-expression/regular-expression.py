import re

text = "The agent's phone number is 408-555-123. Call soon! phone"

pattern_1 = 'phone'

# returns back the first match and the span (start, end)
match = re.search(pattern_1, text)
print(match)

# returns list of all the matches
matches = re.findall(pattern_1, text)
print(matches)

# use iter
for match in re.finditer('phone', text):
    # returns back span (start, end)
    print(match.span())
    # returns back the actual text
    print(match.group())
