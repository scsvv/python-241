# K = input("Type a LOW number: ")
# N = input("Type HIGH number: ")

# try:
#     K, N = int(K), int(N)
#     if N < K:
#         raise IndexError
# except ValueError:
#     print("NonValid data type")
#     exit()
# except IndexError:
#     print(f"N < K: {N}<{K}")
#     exit()

# numbers_sum = 0
# for i in range(K, N+1):
#     if i%2 == 0: 
#         numbers_sum += i
#     print(i)

# print(f'Sum of ntn2 Numbers in Iterval from {N} to {N} equals: {numbers_sum}')



# Пользователь вводит число N. Найдите сумму чисел: 1 + 1.1 + 1.2 + 1.3 + ... + (1 + N / 10).

N = input("Type Value of Number N: ")

try:
    N = int(N)
    if N < 0:
        raise IndexError
except ValueError:
    print("Non-Valid Datd Type")
    exit()
except IndexError:
    print("Value should be under 0")

numbers_sum = 0
for i in range(N+1): 
    numbers_sum += 1 + i/10

print(f"Result: {numbers_sum}")