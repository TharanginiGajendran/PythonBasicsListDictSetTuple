
# Tuples is a collection of items which are indexed, ordered and immutable
# syntax => tuple_name = (item1,item2,item3,.......)
# can have different data types

cars = ("Audi","BMW","Mini Cooper","Benz")
# indexed => can be accessed using index
print(cars)
print(cars[2])

# immutable => cannot modify the value of tuple =>like add,remove,delete
# error
# cars[1] = "Volvo"
# print(cars)

# only can get information from the tuple
print(cars[0])

# can have duplicates like list
animals = ("Dog","Cat","Monkey","Donkey","Dog",1,3)
print(animals)