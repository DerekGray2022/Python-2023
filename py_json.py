# JSON is commonly used with data APIS. Here's how we can parse JSON into a Python dictionary

import json

"""     SAMPLE JSON     """
userJson = '{"first_name": "Jimmy", "last_name": "Jazz", "age": 67}'


''' Parse JSON to Dictionary '''
user = json.loads(userJson)
# print(user)
# print(user['first_name'])

''' Parse Dictionary to  JSON'''
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}
carJSON = json.dumps(car)
print(carJSON)







