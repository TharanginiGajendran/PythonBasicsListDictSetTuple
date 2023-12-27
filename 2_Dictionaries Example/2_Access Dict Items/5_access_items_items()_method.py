
# item is a key-value pair of a dictionary
# returns view object, which contains items(key-value pair) as a list
# view object => reflects any changes done to the dictionary
# syntax  = dict_name.items()
# dictionary methods

car = {"model": "Mini Cooper", "color": "Yellow", "doors": 6}
car_items = car.items()
print(car_items)
car["speed"] = "120km/hr"
print(car_items)