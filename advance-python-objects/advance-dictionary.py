d = {'k1': 1, 'k2': 2}

# dictionary comprehension - This is not the best way to write code as it look complex
c = {x: x ** 2 for x in range(10)}
print(c)

# second type of comprehension - This is not the best way to write code as it look complex

e = {k: v ** 2 for k, v in zip(['a', 'b'], range(2))}

print(e)
