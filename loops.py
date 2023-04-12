# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ["John", "Brian", "Sara", "Susan"]

''' Simple For loop '''
# for person in people:
#     print(f"Current person: {person}")


''' break   '''
# for person in people:
#     if person == "Sara":
#         break
#     print(f"Current person: {person}")

''' continue   '''
# for person in people:
#     if person == "Sara":
#         continue
#     print(f"Current person: {person}")

''' range   '''
# for i in range(len(people)):
#     print(f"Current person: {people[i]}")

''' Custom range    '''
# for i in range(3, 11):
#     print(f"Number: {i}")



# While loops execute a set of statements as long as a condition is true.

count = 5

while count <= 10:
    print(f"Count: {count}")
    count += 1
