# Using a flag
prompt = "\nTell me something, and I'll repeat it back to you:"
prompt += "\Enter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)