# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

"""    VARIABLE ASSIGNMENTS   """
# x = 1                     # int
# y = 2.5                  # float
# name = "Jimmy"     # str
# is_cool = True      # bool


"""   MULTIPLE ASSIGNMENT    """
x, y, name, is_cool = (1, 2.5, "Jimmy", True)

a = x + y


"""   CONSOLE OUTPUT    """
# print(x, y, name, is_cool, a)
"""   Determine Variable Type   """
print(type(y))

"""   CASTING TYPES   """
y = str(y)
print(type(y))
print(y)


