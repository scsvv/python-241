# N = input("N = ")

# try: 
#     N = int(N)
#     if N < 0: 
#         raise IndexError
# except:
#     exit()

# for i in range(1, N*2): 
#     if i <= N:
#         print('*' * i)
#     else: 
#         print('*' * (N*2 - i))

word = input("Type word: ")
reverse = ''
for i in word[::-1]: 
    reverse += i
print(reverse)