# If/ Else conditions are used to decide to do something based on something being true or false

x = 13
y = 28


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

''' Simple IF'''
# if x == y:
#     print(f"{x} is equal to {y}")

''' IF/ELSE'''    
# if x == y:
#     print(f"{x} is equal to {y}")
# else:
#     if x > y:
#         print(f"{x} is greater than {y}")
#     else:
#         print(f"{x} is less than {y}")

''' ELSE IF (elif)  '''
# if x == y:
#     print(f"{x} is equal to {y}")
# elif x > y:
#     print(f"{x} is greater than {y}")
# else:
#     print(f"{x} is less than {y}")

'''Nested IFs  '''
# if x > 2:
#     if x <= 13:
#         print(f"{x} is greater than 2 and less then or equal to 13")


# Logical operators (and, or, not) - Used to combine conditional statements

''' AND '''
# if x > 2 and x <= 13:
#         print(f"{x} is greater than 2 and less then or equal to 13")

''' OR  '''
# if x > 2 or x > 13:
#         print(f"{x} is greater than 2 or greater than 13")

''' NOT '''
# if not (x == y):
#         print(f"{x} is NOT equal to {y}")




# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

''' IN  '''
# x = 3
# numList = [1, 2, 3, 4, 5]

# if x in numList:
#         print(x in numList)

''' NOT IN  '''
# x = 13
# numList = [1, 2, 3, 4, 5]

# if x not in numList:
#         print(x not in numList)




# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

''' IS  '''
# y = 13

# if x is y:
#         print(x is y)

''' IS NOT  '''
y = 43

if x is not y:
        print(x is not y)
