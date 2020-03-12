#sets

s1 = {1, 2, 4}
s2 = {1,4,5,2,6}

print(s1.issubset(s2))


dictionary = dict()
dictionary =dict(john=40, peter=45)
print(dictionary)

# list(dictionary.keys())#: #list	#Returns a dict_keys type of object, that you can convert in a sequence of values with list(dictionary.keys())
# list(dictionary.values())#: #list	#Returns a dict_values type of object, that you can convert with list(dictionary.values())
# list(dictionary.items())#: #tuple	#Returns a dict_items type of object, that you can convert in a sequence of tuples (key, value) with list(dictionary.items()).
# clear()#: None	#Deletes all entries.
# get(key)#: value	Returns the value for the key.
# pop(key)#: value	Removes the entry for the key and returns its value.
# popitem()#: tuple	Returns a randomly-selected key/value pair as a tuple and removes the selected entry