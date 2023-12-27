
# removing an item using popitem() method
# removes last inserted item =>returns a deleted item as a tuple ('Company':'CTG')
# syntax => dict_name.popitem()

user_details = {"Name":"Thara","Id":1,"Company":"CTG"}
user_details.popitem()
print(user_details)
