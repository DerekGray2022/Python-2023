# A List is a collection which is ordered and changeable. Allows duplicate members.

"""     CREATE LIST     """
numbers = [0, 1, 2, 3, 4]
fruits = ["Apple", "Orange", "Banana", "Apricot", "Passion Fruit"]

''' Use a List Constructor  '''
# numbers2 = list((5, 6, 7, 8, 9))

# print(numbers)
# print(numbers2)

''' Retrieve a value from list '''
print(fruits[3])

''' Get Length  '''
print(f"Length: {len(fruits)}")

''' Append to List '''
fruits.append("Mango")
print(f"Append Mango: {fruits}")

''' Remove value from List'''
fruits.remove("Banana")
print(f"Banana removed: {fruits}")

''' Insert into position    '''
fruits.insert(2, 'Strawberry')
print(f"Strawberry inserted @ position 2: {fruits}")

''' Change value    '''
fruits[0] = 'Blueberry'
print(f"Changed first value to Blueberry: {fruits}")

''' Remove from position with pop '''
fruits.pop(2)
print(f"Popped value @ 2 from List: {fruits}")

''' Reverse list    '''
fruits.reverse()
print(f"List reversed: {fruits}")

''' Sort list   '''
fruits.sort()
print(f"List sorted alphabetically: {fruits}")

''' Reverse sort    '''
fruits.sort(reverse=True)
print(f"List reversed: {fruits}")




