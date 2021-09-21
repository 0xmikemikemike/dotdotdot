import wordninja

file1 = open('decodedLines3.txt', 'r')
Lines = file1.readlines()

count = 0
#lm = wordninja.LanguageModel('common_words.txt.gz')
# Strips the newline character
for line in Lines:
    count += 1
    string_to_test = line.strip()

    if len(wordninja.split(string_to_test)) < 12:
        print ("line: " + str(count) + " split: ")
        print (wordninja.split(string_to_test))
