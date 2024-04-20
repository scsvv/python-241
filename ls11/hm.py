def is_prime(number=None):
    if number is None:
        return False
    elif number == 0 or number == 1:
        return True
    
    for i in range(2, number // 2): 
        if number % i == 0:
            return False
    
    return True

print(f"10 = {is_prime(10)}")
print(f"11 = {is_prime(149)}")
print(f"12 = {is_prime(12)}")
print(f"13 = {is_prime(13)}")