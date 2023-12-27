
# use of asterisk in unpacking a tuple
# asterisk is used when number of variable is less than value of tuple .eg 2 variable for 4 items in a tuple
# when this happens, will place asterisk infront of last variable and
# the last variable will receive remaining tuple

cars = ("Audi","BMW","Mini Cooper","Benz","Toyota","Matza","Hyundai","Honda")
car1,car2,car3,car4,*car5 = cars
print(car1)
print(car2)
print(car3)
print(car4)
print(car5)

animal = ("dog","cat","monkey")
*animal1,animal2 = animal
print(animal1)
print(animal2)
