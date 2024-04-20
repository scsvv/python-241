# 3 x 3 => 9! => 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 

def factorial(N):
    if N == 1 or N == 0: 
        return 1
    return factorial(N - 1) * N

print(factorial(9))
