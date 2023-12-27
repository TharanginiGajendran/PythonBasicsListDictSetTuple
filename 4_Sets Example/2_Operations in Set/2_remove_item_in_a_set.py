

# remove()
# case sensitive
# syntax => set.remove(value)

set1 = {1, 3.6, 3, 4, 5, 'Thara', 'School', -12, 23, 'Hanks'}
print(set1)
set1.remove(3)
print(set1)
set1.remove("School")
print(set1)

set1.pop()
print(set1)

# discard()
# syntax => set.discard(value)
set1.discard(1)
print(set1)

# clear()
set1.clear()
print(set1)
