prompt = "\nEnter a word and I'll give you back only consonants:"
prompt += "\n(Enter 'quit' to end the program.) "

while True:
    word = input(prompt)
    word = word.lower()
    
    if word == 'quit':
        break
    else:
        for letter in word:
            if letter == 'a':
                continue
            if letter == 'e':
                continue
            if letter == 'i':
                continue
            if letter == 'o':
                continue
            if letter == 'u':
                continue
            
            print(letter, end="")
            