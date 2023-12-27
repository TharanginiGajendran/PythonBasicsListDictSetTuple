
# access keys using keys() method
# keys()=> returns view object containing keys as a list
# view object => reflects any changes done to the dictionary

#  syntax = dict_name.keys()
# dictionary methods

animal = {"species":"Dog","name":"Dommy","color": "Brown"}
animal_keys = animal.keys()
print(animal_keys)
# can add new keys to the list
animal["eating"] = "bones"
print(animal_keys)