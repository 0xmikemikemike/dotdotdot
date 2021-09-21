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

count = 0
# Strips the newline character
for line in Lines:
    postive_shift_text = shift(line, 1)
    negative_shift_text = shift(line, -1)

    print("{}".format(postive_shift_text))
    print("{}".format(negative_shift_text))
