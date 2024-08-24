favorite_party = {
    'zee':'udp',
    'wali':'pdois',
    'kanjura':'udp',
    'saikou':'udp',
    'kabiro':'npp',
    'galleh':'independent',
    }

# Loop through the dictionary
for name, party in favorite_party.items():
    if party == 'independent':
        print(f"{name.title()}'s political pary is {party.title()}.")
    else:
        print(f"{name.title()}'s political party is {party.upper()}.")
        

# Loop through the keys 
print("\nThe following people participated in the poll:")

for name in sorted(favorite_party.keys()):
    print(name.title())
    

# Loop through the values
print("\nThe following political parties are mentioned:")

for party in sorted(set(favorite_party.values())):
    if party == 'independent':
        print(party.title())
    else:
        print(party.upper())