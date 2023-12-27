
# insert() -> built in method, used to add items in specific position
# syntax = list.append(position,value)

country = ["India","Paris"]
country.insert(1,"South Africa")
# dont do like this
# still works will add element in last
country.insert(10,"Bolivia")
country.insert(0,"Haiti")
print(country)