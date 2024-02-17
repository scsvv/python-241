# attempt = 0
# mock_password = 'Qwerty1!'
# access = False
# while attempt < 3: 
#     password = input("Type your password: ")
#     if mock_password == password:
#         print("Log In")
#         access = True
#         break
#     else:
#         print("Access dined")
#     attempt += 1

# if access: 
#     print("dshfjdfjsjshfkdl")
# else:
#     print("Buy")
#     exit()

# N = input("Type N: ")

# try:
#     N = int(N)
# except ValueError:
#     print("Error data type")
#     exit()

# i = 0
# while i <= N:
#     if i%2 == 0:
#         print(i)
#         i+=2
# result, strf = 1, ''
# while N!=1:
#     result *= N
#     strf += f' {N} *'
#     N -= 1

# print(f'{strf} 1 = {result}')
min_value, max_value = float('inf'), float('-inf')
while True: 
    N = input("Type N: ")

    try:
        N = int(N)
    except ValueError:
        print("Error")
        continue
    
    if N == 0: 
        break

    if max_value < N:
        max_value = N
    
    if min_value > N:
        min_value = N
    
print(min_value, max_value)




