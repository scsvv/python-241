text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod aeaeae tempor incididunt ut labore et dolore magna aliqua. Nunc id cursus metus aliquam eleifend. Pretium quam vulputate dignissim suspendisse in est ante in nibh. Pellentesque habitant morbi tristique senectus et netus. Nisl tincidunt eget nullam non nisi est sit amet. Tincidunt nunc pulvinar sapien et ligula ullamcorper malesuada. Eget velit aliquet sagittis id consectetur purus ut. Id diam vel quam elementum. Nulla facilisi cras fermentum odio. Eleifend mi in nulla posuere. Orci dapibus ultrices in iaculis nunc."
text = text.split(" ")

print(f"Quantity of words: {len(text)}")

max_length = ""
max_prounce, max_prounce_word = 0, ""
for word in text: 
    if len(max_length) < len(word):
        max_length = word
    
    counter = 0
    
    for letter in word:
        letter = letter.lower()
        if letter == 'a' or letter == 'e' or \
            letter == 'i' or letter == 'i' or \
            letter == 'o' or letter == 'u':
            counter += 1
    
    if counter > max_prounce:
        max_prounce = counter
        max_prounce_word = word

print(f'The longest word in the text is: {max_length} with {len(max_length)} letters')
print(f'{max_prounce_word} contain {max_prounce}')