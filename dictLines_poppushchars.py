import wordninja
import base64
import binascii

file1 = open('decodedLines3.txt', 'r')
Lines = file1.readlines()

count = 0

#lm = wordninja.LanguageModel('common_words.txt.gz')
# Strips the newline character
for line in Lines:
    count += 1
    
    string_to_test = line.strip().lower()
    
    for x in range(32):
        string_to_test = string_to_test[1:] + string_to_test[0]
        
        split_string = wordninja.split(string_to_test)

        if len(split_string ) < 11:
            print ("line: " + str(count) + "shift: " + str(x) + " split: ")
            print (split_string)
