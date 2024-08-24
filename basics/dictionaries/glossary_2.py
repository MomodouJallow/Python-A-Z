# Now that you know how to loop through a dictionary, clean
# up the code from glossary.py by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.

glossary = {
    'variable':'label for a value',
    'string':'sequence of characters',
    'list':'collection of items',
    'method':'action taken on a value',
    'tuple':'an immutable list',
    }


# Add more terms
glossary['set'] = 'collection of unique items'
glossary['boolean values'] = 'true and false'
glossary['concatenation'] = 'joining values together'
glossary['dictionary'] = 'key-value pair data structure'
glossary['keyword'] = 'reserved names in python'


# Loop through key-value pairs
for word, meaning in glossary.items():
    print(f"\n{word.title()}: {meaning}")