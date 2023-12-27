
#
animals = ["dog","cat","monkey","cow","donkey"]
filtered_animals = [ani.title() for ani in animals]
print(filtered_animals)

# flattening a nested list
print("**********flattening nested loop")
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatenning = [ j for i in nested_list for j in i]
print(flatenning)

# empty_list = []
# for i in nested_list:
#     for j in i:
#         empty_list.append(j)
#
# print(empty_list)

# squaring a number
print("************squaring a number")
# number = int(input("enter number: "))
square = [i*i for i in range(6)]
print(square)

# filtering a even number
print("***********even number")
num = range(0,20)
even = [i for i in num if i % 2 == 0]
print(even)
