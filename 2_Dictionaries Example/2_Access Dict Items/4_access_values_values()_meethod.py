
# access value using values() method
# returns view object which contains values as a list
# syntax = dict_name.values()
# dictionary methods

car = {"model": "Mini Cooper", "color": "Yellow", "doors": 6}
car_values = car.values()
print(car_values)
car["speed"] = "120km/hr"
print(car_values)
