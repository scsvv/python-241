"""
Math: * / // % + - 
EQUALS: == != > < >= <=


Logic: True False => and / or / not 
"""

# username = "scsvvv"
# password = "qwerty"

# type_username = input("Type your username: ")
# type_password = input("Type your password: ")

# if type_username == username and type_password == password:
#     print("You are loggined")
# else:  print("Access dinned")

"""
if else 
try except 

while for 
... 
"""
# a = input("Type A: ")
# b = input("Type B: ")

# try: 
#     a = int(a)
#     b = int(b)
# except: 
#     print("Non-valid datatype")
#     exit()

# if a > b:
#     print(f"{a} > {b}")
# elif a == b: 
#     print(f"{a} == {b}")
# else:
#     print(f"{a} < {b}")
# from math import floor, log10

# a = input("Type number: ")

# try:
#     a = int(a)
# except:
#     print("Non-Valid Data")
#     exit()

# if a > 999 and a < 10000:
#     print(f"Number {a} have 4 numeral")
# else: 
#     print(f"Number {a} have {floor(log10(a))} numeral")



from datetime import datetime

current_day = datetime.now()
text = f"Today is {current_day.strftime('%A')} {current_day.strftime('%d')}th {current_day.strftime('%B')}. And today is a "
if current_day.strftime("%w") == '0' or current_day.strftime("%w") == '6':
    text += "Holiday"
else: 
    text += "Workday"

print(text)