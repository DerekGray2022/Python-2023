# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

''' Create Class    '''
class User:
    ''' Constructor '''
    def __init__(self, name, email, age) -> None:
        self.name = name
        self.email = email
        self.age = age

    def Greeting(self):
        return f"My name is {self.name} and I am {self.age} years old."
        
    def has_birthday(self):
        self.age += 1

''' Extended Class  '''
class Customer(User):
    ''' Constructor '''
    def __init__(self, name, email, age) -> None:
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def Greeting(self):
        return f"My name is {self.name} and I am {self.age} years old. My balance is £{self.balance}"

    def set_balance(self, balance):
        self.balance = balance




''' Initiate User object    '''
jim = User("Jimmy Jazz", "jimmy@jazz.io", 45)
''' Initiate Customer Object    '''
janet = Customer("Janet Jones", "janet@jones.com", 27)

janet.set_balance(500.01)

jim.has_birthday()
print(jim.Greeting())
print(janet.Greeting())




