
# split() methods splits a string into substring
# syntax = string.split(separator,maxsplit)

word = "this is a beautiful shop"
split = word.split(" ")
join = "-".join(split)
print(join)

# just using split method
# which put all the string in the list
language = "Learn all the language"
split_language = language.split()
print(split_language)

# accepting a list of numbers is easier with split()
# split() method applied on string and separated based on spaces
numbers = input("Enter a list of numbers: ").split()
print(numbers)
