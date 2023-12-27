
# assignment operator cannot be used to copy mutable object
# what we are updating in the copy should not be updated in the original dictionary

# should not happen like this
user_details = {"Name":"Thara","Id":1,"Company":"CTG"}
user_copy = user_details
print(user_copy)
user_copy["Name"] = "Tharangini"
print(user_copy)
print(user_details)
print(id(user_copy))
print(id(user_details))