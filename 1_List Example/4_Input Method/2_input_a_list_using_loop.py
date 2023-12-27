
# lets input list of numbers and get a numbers in a list like this [1,2,3]

numbers = input("Enter List of number: ")
print(numbers)

# we are getting this below
# 11 22 33
# 01234567

# what we want
# 11 22 33
# [0  1  2]

# to get above -> input a list using loops

n = int(input("Enter how many numbers in a list: "))
num = []
for i in range(n):
    value = int(input())
    num.append(value)

print(num)
