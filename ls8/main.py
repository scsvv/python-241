import json
vocabulary = dict()

print("""Vocabulary app
Please type your words in format: 

WORD: translate, translate, translate....

For exit from program type 42
""")

with open('output.json', 'r') as file:
    file_contents = file.read()
vocabulary = json.loads(file_contents)

while True:
    data = input("Enter words 👇🏻\n")

    if data == "42":
        break
    elif data == "show":
        print(vocabulary)
        continue

    data = data.split(':')
    
    if len(data) != 2:
        print("Try again")
        continue
    
    word = data[0] 
    translate = data[1].replace(' ', '').split(',')

    if vocabulary.get(word):
        vocabulary[word] = vocabulary[word] + translate
        continue
    vocabulary[word] = translate

output = json.dumps(vocabulary)
with open('output.json', 'w') as file:
    file.write(output)