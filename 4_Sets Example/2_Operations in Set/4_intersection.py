
# intersection
# intersection of two sets contain common elements from both sets


set1 = {1,2,3,4}
set2 = {1,2,3,45,6}

inter_set = set1.intersection(set2)
# or inter_set = set1 & set2
print(inter_set)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set2.intersection_update(set1)
# After this operation, set2 will be modified to contain the intersection of set1 and set2.

print(set2)
