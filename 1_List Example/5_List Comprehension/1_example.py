
# create a list
names = ["Thara","Tharangini","John","James","Jimmy"]
# from the list create a new list which only contains names starts with capital J
j_names = []
t_names = []

# to iterate through the list
for name in names:
    if "J" in name:
        j_names.append(name)
    else:
        t_names.append(name)

print(j_names)
print(t_names)

# lets see how to use list comprehension and reduce the number of lines
# syntax = [expression for item in iterable if condition == True]
# if condition satisfies proceed
# expression represents some value stored inside this list which is single item in a list
# condition checking is optional

names_person = ["John","Lou","Henry","Louis","Laden"]
l_names = [names for names in names_person if "L" in names]
print(l_names)

words = ["one","two","box","book"]
copy_words = [i for i in words]
print(copy_words)