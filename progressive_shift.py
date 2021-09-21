def shift(plain_text, multiplier):
    encrypted_text = ''
    for i in range(len(plain_text)):
        if plain_text[i] == ' ':
            encrypted_text = encrypted_text + plain_text[i]
        elif plain_text[i].isupper():
            encrypted_text = encrypted_text + chr((ord(plain_text[i])+(i*multiplier)-65)%26+65)
        else:
            encrypted_text = encrypted_text + chr((ord(plain_text[i])+(i*multiplier)-97)%26+97)
    return encrypted_text


file1 = open('decodedLines3.txt', 'r')

Lines = file1.readlines()
l = 1
# Strips the newline character
for line in Lines:
    k1 = postive_shift_text = shift(line, 1)
    k2 = negative_shift_text = shift(line, -1)
    if len(wordninja.split(k1)) <= 12:
        print('pos')
        print(l)
        print(wordninja.split(k1))
    if len(wordninja.split(k2)) <= 12:
        print('neg')
        print(l)
        print(wordninja.split(k2))
    l += 1
