
# subset and superset
# valuse from set2 should be contained in set1, if one number is different its false


set1 = {1,2,3,4,5}
set2 = {1,2,3,6}

is_subset = set2.issubset(set1)
print(is_subset)

is_superset = set1.issuperset(set2)
print(is_superset)
