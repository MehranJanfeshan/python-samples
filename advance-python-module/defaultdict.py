from collections import defaultdict

d = defaultdict(lambda: 1000)

d['correct'] = 100

# it always returns back default value, if you ask for a key that does not exists
print(d['wrong'])
