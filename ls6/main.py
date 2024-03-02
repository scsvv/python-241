# cities = list()
# print(f'cities: {cities}')
# for i in range(5):
#     city_name = input("Type city name: ")
#     cities.append(city_name)
#     print(f'cities after adding {city_name}: {cities}')

# print(cities)

# a = [1, 2, 4, 5, 6, 7, 8]
# print(a[0])

# numbers = list()
# for i in range(2, 22, 2):
#     numbers.append(i)

# for number in numbers:
#     print(number)

# print(numbers[2:5])

# from random import randint
# numbers = list()
# for i in range(10):
#     numbers.append(randint(1, 10))

# print(numbers)
# numbers.clear()
# print(numbers)

# text = input("type text: ")
# result = ''
# for letter in text:
#     if letter == 'a' or letter == 'o' or  letter == 'e':
#         continue
#     result += letter
# print(result)

# a = [1, 3, 4, 5]
# b = [4, 5, 6, 7]

# for el in a:
#     if not b.count(el) == 0:
#         for i in range(b.count(el)):
#             b.remove(el)

# print(b)



from random import randint
numbers = list()
for i in range(10):
    numbers.append(randint(1, 10))

print(numbers)
# print(f'\nMax Value: {max(numbers)}, Min Value: {min(numbers)}, SUM = {sum(numbers)}, E = {sum(numbers) / len(numbers)}')

# left, right, index = -1, -1, -1
# for i in range(1, len(numbers) -1): 
#     if(numbers[i] - numbers[i-1] + numbers[i] - numbers[i+1] > left + right):
#         left = numbers[i] - numbers[i-1]
#         right = numbers[i] - numbers[i+1]
#         index = i

# print(index)
result_list = []
for number in numbers:
    if numbers.count(number) > 1:
        result_list.append(number)

result_list.sort()
print(result_list)