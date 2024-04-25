# Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or any-
# thing else you’d like. Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.

languages = ['java', 'python', 'c', 'scala', 'go', 'javascript', 'r']
print(languages)

# Appending an item to end of the list
languages.append('haskell')
print(languages)

# Inserting an item in a specific position in the list
languages.insert(0, 'c#')
print(languages)

# Remove an item from the list using the del statement
del languages[7]  # Remove 'r'
print(languages)

# Popping an item from the end of the list
popped_item = languages.pop()
print(languages)

print(f"\n{popped_item.title()} is removed from the end of the list.")

print()

# Popping an item in any position in the list
languages.pop(4)  # Remove 'scala'
print(languages)

# Remove an item by value
languages.remove('c') # Remove 'c'
print(languages)

print()

# Sort the list temporarily in alphabetical order
print(sorted(languages))

# Sort the list in temporarily in reverse alphabetical order
print(sorted(languages, reverse=True))

print()

# Reverse the order of the list
print("Here is the original list:")
print(languages)

print("\nHere is the reversed list:")
languages.reverse()
print(languages)

print("\nHere is the original list again:")
languages.reverse()
print(languages)

print()

# Sort the list permanently in alphabetical order
languages.sort()
print(languages)

# Sort the list permanently in reverse alphabetical order
languages.sort(reverse=True)
print(languages)

# Find the length of the list
print(f"\nThe lenght of the list is {len(languages)}.")