# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

''' Create Dictionary   '''
person = {
    "first_name": "Jimmy",
    "last_name": "Jazz",
    "age": 58
}

# print(person)
# print(type(person))

''' Use Constructor '''
person2 = dict(first_name="Junko", last_name="Partner", age=87)

# print(person2)
# print(type(person2))

''' Get Value   '''
# print(person["first_name"])
# print(person.get("last_name"))

''' Add Key/Value   '''
person["phone"] = "555 555 5555"
# print(person)

''' Get Dictionary Keys '''
# print(person.keys())

''' Get Dictionary Items '''
# print(person.items())

''' Get Dictionary Values '''
# print(person.values())

''' Copy Dictionary'''
person3 = person.copy()
# print(f"Person: {person}")
person3["City"] = "Srinagar"
# print(f"Person3: {person3}")

''' Delete item '''
del person["age"]
# print(person)
person.pop("phone")
# print(person)

''' Clear Dictionary    '''
person3.clear()
# print(person3)

''' Get Length  '''
# print(len(person2))

''' List of Dictionaries    '''
people = [
    {"name": "Ruby", "age": 37},
    {"name": "Joeleen", "age": 25}
]
print (people)
print(people[0]["name"])





