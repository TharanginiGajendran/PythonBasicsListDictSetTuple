
# not directly possible to add items to tuple, as tuples are immutable
# workaround: convert tuple -> list -> add items to list -> convert list back to tuple

# tuple
cars = ("Audi","BMW","Mini Cooper","Benz")
# convert to list
temp_store = list(cars)
print(temp_store)
temp_store.append("Ferrari")
print(temp_store)
temp_store.insert(0,"Toyota")
print(temp_store)
cars = tuple(temp_store)
print(cars)