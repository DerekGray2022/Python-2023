# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

''' Create Function '''
# def sayHello(name="Billy-Bob"):
#     print(f"Hello, {name}")

# sayHello("Jimmy Jazz")

''' Return values'''
# n1 = 5
# n2 = 18

# def getSum(num1, num2):
#     return num1 + num2

# print(f"{n1} + {n2} = {getSum(n1, n2)}")



# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2
print(getSum(17, 65))

