duplicates = [1, 2, 1, 8, 7, 3, 5, 3, 2, 9, 4, 3, 10, 1]
uniques = []

for duplicate in duplicates:
    if duplicate not in uniques:
        uniques.append(duplicate)
        
print(uniques)