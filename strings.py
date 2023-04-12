# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


"""     STRING FORMATTING       """
name = "Jimmy"
age = 54
''' Concatenate '''
# print("Hello, my name is " + name + " and I am " + str(age) + " years old.")

'''     Arguments by Position       '''
# print("Hello, my name is {name} and I am {age} years of age.".format(name=name, age=age))

'''     F Strings ( only available in Python3.6+ )       '''
# print(f"Hello, my name is {name} and I am {age} years old.")




"""     STRING METHODS      """
s = "hello world"

''' Capitalise the first letter '''
print(s.capitalize())

''' Make all uppercase  '''
t = s.upper()
print(t)

''' Make all lower  '''
print(t.lower())

''' Swap case   '''
u = "Hello World."
print(u.swapcase())

''' Get length  '''
print(len(s))

''' Replace '''
print(s.replace('world', 'everyone'))

''' Count   '''
sub = 'l'
print(s.count(sub))

''' Starts with '''
print(s.startswith('hello'))

''' Ends with   '''
print(s.endswith('d'))

''' Split into a array of individual words (equivalent to explode(" ", s);)   '''
print(s.split())

''' Find position   '''
print(s.find('r'))

''' Is all alphanumeric '''
print(s.isalnum())

''' Is all alphabetic   '''
print(s.isalpha())

''' Is all numeric  '''
print(s.isnumeric())


