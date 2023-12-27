
# copy dictionary using copy() method
#syntax => dict_name2 = dict_name.copy()

user_details = {"Name":"Thara","Id":1,"Company":"CTG"}
user_copy = user_details.copy()
print(user_copy)
user_copy["Name"] = "Tharangini"
print(user_copy)
print(user_details)