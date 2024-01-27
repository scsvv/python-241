# a = input("Enter A: ")
# b = input("Enter B: ")
# print((int(a)%2) == (int(b)%2))

# password = input("Enter new password: ")
# retype_password = input("Retype your new password: ")
# print(password == retype_password)


number = input("Enter number: ")
number = int(number)
left, rigth = number // 10, number % 10
print(left + rigth)