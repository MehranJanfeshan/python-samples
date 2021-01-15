s = set()

s.add(1)
s.add(2)

# make a copy of set
sc = s.copy()

# Clear the set
s.clear()

# returns back the differences between two sets
s.difference(sc)

# remove the similar items from s2
s1 = {1, 2, 3}
s2 = {1, 4, 5}
s1.difference_update(s2)
print(s1)

# removes and item from the set
s1.discard(3)

print(s1)

# returns back the intersections between two sets
s1 = {1, 2, 3}
s2 = {1, 4, 5}
print(s1.intersection(s2))

# update the set with the intersection - this changes the original set
s1.intersection_update(s2)
print(s1)

# joint
s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}

print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

# check if a set is subset of another set
s1 = {1, 2}
s2 = {1, 2, 4}

print(s1.issubset(s2))

# check if a set contains another set

s1 = {1, 2}
s2 = {1, 2, 4}

print(s2.issuperset(s1))

# return back the symmetric difference
s1 = {1, 2}
s2 = {1, 2, 4}

print(s1.symmetric_difference(s2))

# return back the union
s1 = {1, 2}
s2 = {1, 2, 4}

print(s1.union(s2))



