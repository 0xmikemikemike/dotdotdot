import wordninja
import base64
import binascii

file1 = open('decodedLines3.txt', 'r')
Lines = file1.readlines()

count = 0

alpha_map = {
    'a':'z', 
    'b':'y', 
    'c': 'x',
    'd': 'w',
    'e': 'v', 
    'f': 'u', 
    'g': 't', 
    'h': 's', 
    'i': 'r', 
    'j': 'q', 
    'k': 'p', 
    'l': 'o', 
    'm': 'n', 
    'n': 'm', 
    'o': 'l', 
    'p': 'k', 
    'q': 'j',
    'r': 'i',
    's': 'h',
    't': 'g',
    'u': 'f',
    'v': 'e',
    'w': 'd', 
    'x': 'c',  
    'y': 'b', 
    'z': 'a'}

#lm = wordninja.LanguageModel('common_words.txt.gz')
# Strips the newline character
for line in Lines:
    count += 1
    
    string_to_test = ' '.join(map(str, [alpha_map.get(c) for c in line.strip().lower()]))
    
    if len(wordninja.split(string_to_test)) < 12:
        print ("line: " + str(count) + " split: ")
        print (wordninja.split(string_to_test))