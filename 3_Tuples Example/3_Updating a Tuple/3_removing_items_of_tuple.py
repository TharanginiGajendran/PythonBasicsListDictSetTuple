
# cannot remove items as tuples are immutable
# workaround: convert tuple -> list -> remove items of a list -> convert list back to tuple

cars = ("Audi","BMW","Mini Cooper","Benz","Toyota","Hyundai")
temp_remove = list(cars)

temp_remove.remove("Audi")
print(temp_remove)

temp_remove.pop(2)
print(temp_remove)

del temp_remove[3]
print(temp_remove)

temp_remove.pop()
print(temp_remove)

cars = tuple(temp_remove)
print(cars)


