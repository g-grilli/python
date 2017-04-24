#Uppercase a string
greeting = "Good morning".upper()
print(greeting)

#Capitalize a string
greeting = "good morning".capitalize()
print(greeting)

#Reverse a string
greeting = "Good Morning"
greeting[::-1]
print(greeting[::-1])

#Leetspeak
gibberish = "THIS PARAGRAPH IS PRACTICE FOR CHANGING CHARECTERS IN A STRING"
gibberish = gibberish.replace('A', '4',)
gibberish = gibberish.replace('E', '3',)
gibberish = gibberish.replace('G', '6',)
gibberish = gibberish.replace('I', '1',)
gibberish = gibberish.replace('O', '0',)
gibberish = gibberish.replace('S', '5',)
gibberish = gibberish.replace('T', '7',)
print(gibberish)

#Long-long Vowels
word = input("Please enter a word? ")
if "oo" in word:
  word = word.replace("oo", "ooooo")
if "ee" in word:
    word = word.replace("ee", "eeeee")
print(word)
#long vowels answer sheet
#word = word.replace('ee', 'eeeee')
#word = word.replace('oo', 'ooooo')
#print(word)

#Caesar Cipher
caesar = "lbh zhfg hayrnea jung lbh unir yrnearq"
broken_code = ''
for i in caesar:
    if i == 'b':
        broken_code += 'o'
    elif i == 'c':
        broken_code += 'p'
    elif i == 'd':
        broken_code += 'q'
    elif i == 'e':
        broken_code += 'r'
    elif i == 'f':
        broken_code += 's'
    elif i == 'g':
        broken_code += 't'
    elif i == 'h':
        broken_code += 'u'
    elif i == 'i':
        broken_code += 'v'
    elif i == 'j':
        broken_code += 'w'
    elif i == 'k':
        broken_code += 'x'
    elif i == 'l':
        broken_code += 'y'
    elif i == 'm':
        broken_code += 'z'
    elif i == 'n':
        broken_code += 'a'
    elif i == 'o':
        broken_code += 'b'
    elif i == 'p':
        broken_code += 'c'
    elif i == 'q':
        broken_code += 'd'
    elif i == 'r':
        broken_code += 'e'
    elif i == 's':
        broken_code += 'f'
    elif i == 't':
        broken_code += 'g'
    elif i == 'u':
        broken_code += 'h'
    elif i == 'v':
        broken_code += 'i'
    elif i == 'w':
        broken_code += 'j'
    elif i == 'x':
        broken_code += 'k'
    elif i == 'y':
        broken_code += 'l'
    elif i == 'z':
        broken_code += 'm'
    elif i == 'a':
        broken_code += 'n'
    elif i == ' ':
        broken_code += ' '
print(broken_code)
