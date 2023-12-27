
 # symmetric difference
 # contains elements from which are unique to ecah other from both sets



set1 = {1,2,3,4,5}
set2 = {1,2,3,45,6}

# prints => 4,5,45,6

sym_diff = set1.symmetric_difference(set2)
# or set1 ^ set2
print(sym_diff)
