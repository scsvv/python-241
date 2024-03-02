# prices_l = [("apple", 12), ("banana", 23), ("orange", 26)]

# search = 'appl'

# for item in prices_l:
#     if item[0] == search:
#         print("founded")
#         break


# items = {
#     "apple": 12,
#     "banana": 23,
#     "orange": 32,
#     "grape": 43, 
#     "cherry": 43,
# }

# search = "apple"
# print(items.get(search))

items = dict()
N = input("Enter your data: ")
try: 
    N = int(N)
except ValueError:
    N = 0

# for i in range(N):
#     name = input("Type product name: ")
#     count = input("Type product quantity: ")
#     items[name] = count

# print(items)

for i in range(N):
    name = input("Type friend's name: ")
    age = input("Type friend's age: ")
    try: 
        age = int(age)
    except ValueError:
        age = None
    items[name] = age

print(items)

maximum_age = ['', -1]
for item in items.items():
    if not item[1]: 
        continue
    if item[1] > maximum_age[1]:
        maximum_age = item

print(maximum_age)
