# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

'''     Create Tuple        '''
fruits = ("Apple", "Orange", "Banana", "Apricot", "Passion Fruit")
fruits2 = tuple (("Mango", "Pineapple", "Lychee", "Rasberry", "Peach"))

# print(fruits)
# print(fruits2)

''' Single value needs trailing comma   '''
fruits3 = ("Apple",)
# print(fruits3, type(fruits3))

# print(fruits2[3])

''' Can't change the value'''
# fruits[3] = "Grape"

''' Delete Tuple'''
del fruits3

# print(fruits3)

''' Get Length  '''
# print(len(fruits))



# A Set is a collection which is unordered and unindexed. No duplicate members.

''' Create Set  '''
cars = {"Volvo", "Mercedes", "Audi", "Rolls Royce", "Ford"}

''' Check if value exists in Set    '''
print("Ford" in cars)

''' Add to Set  '''
cars.add("Citroen")
print(cars)

''' Remove from Set '''
cars.remove("Citroen")
print(cars)

''' Clear Set   '''
cars.clear()
print(cars)

''' Delete Set'''
del cars
# print(cars)





