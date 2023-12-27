
# difference
# difference of two sets contains elements from set one and not in set2


set1 = {1,2,3,4,5}
set2 = {1,2,3,45,6}

# prints => 4,5

diff_set = set1.difference(set2)
# or diff-set = set1 - set2
print(diff_set)



# after this set4 contains only elements from difference
set3 = {1,2,3,4,5}
set4 = {1,2,3,45,6}

set4.difference_update(set3)
print(set4)




