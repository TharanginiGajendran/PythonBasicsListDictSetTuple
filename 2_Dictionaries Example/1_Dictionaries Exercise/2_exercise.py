# dictionaries
# cannot have same key for 2 items, duplicate are not allowed
car = {
    "name": "Audi",
    "model": "Q7",
    "name": "BMW"
}
# same key for 2 items => but only one value is stored
# key value pair which comes later will always be available in the dictionary
print(car)

# dictionaries are mutable

user_details = {"name": "Thara", "id": "1"}
user_details["name"] = "Tharangini Gajendran"
print(user_details)

# LENGTH OF THE DICTIONARY
# the length is determined using len()
# gives the count of key value pair

animal = {"name": "Dommy", "age": 4,"color": "Brown" }
print(len(animal))
