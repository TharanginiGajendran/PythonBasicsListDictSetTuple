import copy


# index()
# give the index of value
# syntax = list.index(value)
print("******************index()")
numbers = [1,2,2,3,4,5,6,7,8]
index_value = numbers.index(2)
print(index_value)

#count()
# count the number of values presented
# syntax = list.count(value)
print("************count()")
num = [1,2,3,4,2,6,2,8,9]
print(num.count(2))

# sort()
# sort num in ascending order
print("**********sort() ascending order")
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
my_list.sort()
print(my_list)

print("************sort()descending order")
my_list.sort(reverse=True)
print(my_list)

# reverse()
# reversing a number
print("***********reverse()")
num_rev = [1,2,3,5,6,7,9]
num_rev.reverse()
print(num_rev)

# copy
# not printing the original list,printing copied list
print("******************copy()")
num_copy = [1,2,3,4,5,6,7]
duplicate = num_copy.copy()
# duplicate[0] = 10
# num_copy[0] = 30
# print(num_copy)
print(duplicate)

print("******************copy() slicing")
original_list = [1, 2, 3, 4, 5]
copied_list = original_list[:]
print(copied_list)

print("*******************copy() list()constructor")
original_list = [1, 2, 3, 4, 5]
copied_list = list(original_list)
print(copied_list)

# using copy module to copy
# need to import copy
print("***********copy() Module")
module_list = [1,2,3,4,5,6,7,8,9]
copy_module = copy.copy(module_list)
print(copy_module)

# deepcopy
print("************copy() deepcopy")
deep_copy = copy.deepcopy(module_list)
print(deep_copy)




