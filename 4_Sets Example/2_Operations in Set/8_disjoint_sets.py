
# disjoint sets
# true, if both elements dont have any common elements


set1 = {1,2,3,4}
set2 = {1,2,3,45,6}

are_disjoint = set1.isdisjoint(set2)
print(are_disjoint)

set1 = {1,2,3,4}
set2 = {45,6}
dis = set1.isdisjoint(set2)
print(dis)