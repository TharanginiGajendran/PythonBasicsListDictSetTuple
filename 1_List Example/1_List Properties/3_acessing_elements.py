
# access elemets using indexing from 0 to last

numbers = [1,2,3,4,5,6,7,8,9]

# access elements from start
print("*********first_index(positive index)")
print(numbers[0])
print(numbers[1])
print("********************")
# access elements from last
print("*********last_index(negative index)")
# prints 9
print(numbers[-1])
# prints 8
print(numbers[-2])
print("********************")


print("\n")
print("*********numbers from first to last using negative index)")
print(numbers[ : -1])
print("********************")

print("*********numbers from descending order using negative index)")
print("reversed slicing")
print(numbers[ :: -1 ])
print("********************")





