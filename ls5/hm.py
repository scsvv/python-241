N = input("Enter N: ")
try:
    N = int(N)
    if N < 1:
        raise IndexError
except ValueError:
    print("Value Error, not int data type")
    exit()
except IndexError:
    print("N < 1")
    exit()

strf, result = '', 0
for i in range(1, N+1):
    result += 1/i
    if i == 1: 
        strf += f'1 '
        continue    
    strf += f'+ 1/{i} '

print(f'{strf}= {result:.2f}')
