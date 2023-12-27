
# copy dictionary using dict() method
# syntax => dict_name2  = dict(dict_name1)

user_details = {"Name":"Thara","Id":1,"Company":"CTG"}
user_copy = dict(user_details)
print(user_copy)
user_copy["Name"] = "Tharangini Gajendran"
print(user_copy)
print(user_details)