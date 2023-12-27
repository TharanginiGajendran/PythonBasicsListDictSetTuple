
# extend() -> built in method,add items of one list in another list
# syntax = list1.extend(list2)

numbers_list1 = [1,2,3]
print("*********before extend() method")
# print(numbers_list1)
numbers_list2 = [4,5,6]
print(numbers_list2)
print("***********after extend() method")
numbers_list1.extend(numbers_list2)
# numbers_list2.extend(numbers_list1)
print(numbers_list1)
print(numbers_list2)
