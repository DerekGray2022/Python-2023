# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

''' Core Modules    '''
import datetime
from datetime import date

''' PIP Modules '''
from camelcase import CamelCase

''' Custom Modules  '''
from validator import validate_email

time = datetime.datetime.now()
today = date.today()

now = time.strftime("%H : %M : %S")

c = CamelCase()
# print(c.hump("hello there world"))

# print(f"Today is {today} and the time is {now}")

email = "test@test.com"
if validate_email(email):
    print(f"The email {email} is VALID")
else:
    print(f"The email {email} is INVALID")





