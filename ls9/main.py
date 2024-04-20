# mock = [{'password': '123', 'login': 'scsvv'}, {'password': '321', 'login':'xawav'} ]

# login = input("Login: ")
# password = input("Password: ")

# def password_check(p1, p2):
#     return p1==p2 


# for item in mock:
#     if item.get('login') == login:
#         for i in range(3):
#             if password_check(
#                 password, item.get('password')):
#                 print('Welcome')
#                 break
#         else: 
#             print('Access dined')
#             break
# else: 
#     print(f"Don't have user {login} in system")


# def circle(radius=None):
#     if radius:
#         return f'{(3.1415 * radius ** 2):.2f}' 
#     return None

# r1 = circle(3)
# print(r1)

# def three(number=1):
#     return number%3==0

# print(three(0))
# print(three(3))
# print(three(4))
# print(three(5))
# print(three(6))
# print(three())

# def max_list(numbers=None):
#     if not numbers or not isinstance(numbers, list) or \
#         len(numbers) == 0:
        
#         return None
    
#     if len(numbers) == 1:
#         return numbers[0]
    
#     return max(numbers)

# n1 = max_list([1, 2, 3, 4, 5, 6])
# n2 = max_list('asdff')

# print(n1, n2)

def even_counter(numbers=None):
    if not numbers or not isinstance(numbers, list) or \
        len(numbers) == 0:
        
        return 0
    
    count = 0
    for number in numbers:
        if number%2==0:
            count+=1
    return count

n1 = even_counter([1, 2, 3, 4, 5, 6])
n2 = even_counter('asdff')
print(n1, n2)