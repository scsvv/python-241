from random import randint

score = 0

for i in range(5):
    num1, num2 = randint(0, 100), randint(0, 100)
    q1 = input(f"Type answer to {num1} + {num2} = ")

    try: 
        q1 = int(q1)
    except ValueError:
        q1 = None

    if q1 is None or q1 != (num1 + num2):
        pass
    else: 
        score += 1

if score > 3: 
    print("U pass u exam")
else: 
    print("Next time")
    
