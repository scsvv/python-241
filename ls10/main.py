from math import log10, floor

roman_numbers = {
    '0': ["I", "V"], 
    '1': ["X", "L"], 
    '2': ["C", "D"],
    '3': ["M"]
}

roman_numbers_values = {
    "I": 1, 
    "V": 5, 
    "X": 10,
    "L": 50, 
    "C": 100, 
    "D": 500, 
    "M": 1000,    
}

def parser(num, dec):
    if num < 4:
        return f'{roman_numbers.get(str(dec))[0]*num}'
    if num == 4:
        return f'{roman_numbers.get(str(dec))[0]}{roman_numbers.get(str(dec))[1]}'
    if num > 4 and num < 9:
        return f'{roman_numbers.get(str(dec))[1]}{roman_numbers.get(str(dec))[0]*(num%5)}'
    if num == 9:
        return f'{roman_numbers.get(str(dec))[0]}{roman_numbers.get(dec+1)[0]}'

def from_arabic_to_roman_conv(number=None):
    if number is None or not isinstance(number, int) or number < 0 or number > 4000:
        return None
    
    if number < 10:
        return parser(number, 0) 
    
    dec = floor(log10(number))
    left = number // 10 ** dec
    number = number % 10 ** floor(log10(number))
    
    return f'{parser(left, dec)}{from_arabic_to_roman_conv(number)}'

def from_roman_to_arabic_number(fstr): 
    data, pointer = 0, 0
    k = len(fstr)
    while k > 0:
        curr = roman_numbers_values[fstr[k-1]]
        if curr < pointer:
            curr = - curr
        data += curr
        k -=1
        pointer = curr
    return data


num = from_arabic_to_roman_conv(2024)
print(num)
data = from_roman_to_arabic_number(num)
print(data)

data = from_roman_to_arabic_number("MMIX")
print(data)