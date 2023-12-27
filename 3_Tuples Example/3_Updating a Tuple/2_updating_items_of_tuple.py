
# cannot update as tuples are immutable
# # workaround: convert tuple -> list -> update items of a list -> convert list back to tuple

cars = ("Audi","BMW","Mini Cooper","Benz")
# convert to list
temp_update = list(cars)
temp_update[0] = "Toyota"
temp_update[3] = "Hyundai"
print(temp_update)

cars = tuple(temp_update)
print(cars)