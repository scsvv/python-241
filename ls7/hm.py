from random import randint

arr = list()

for i in range(0, 10):
    arr.append(randint(1, 10))

print(arr)

# first_max, second_max = arr[0], arr[0]

# for el in arr:
#     if el > first_max: 
#         first_max, second_max = el, first_max
#     elif el > second_max and el < first_max: 
#         second_max = el

# print(first_max, second_max)

arr = list(set(arr))
print(arr)