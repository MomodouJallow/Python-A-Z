voter_0 = {'name':'zee', 'party':'udp'}
voter_1 = {'name':'wali', 'party':'pdois'}
voter_2 = {'name':'kabiro', 'party':'npp'}
voter_3 = {'name':'saikou', 'party':'udp'}
voter_4 = {'name':'galleh', 'party':'independent'}
voter_5 = {'name':'kanjura', 'party':'udp'}

voters = [voter_0, voter_1, voter_2, voter_3, voter_4, voter_5]

for voter in voters:
    if voter['party'] == 'independent':
        print(f"{voter['name'].title()} voted for {voter['party'].title()}.")
    else:    
        print(f"{voter['name'].title()} voted for {voter['party'].upper()}.")
        

print("\nThe following people voted:")
for voter in voters:
    print(f"{voter['name'].title()}")
    

print("\nThe following political parties participated:")

parties = []

for voter in voters:
    if voter['party'] not in parties:
        parties.append(voter['party'])
        
for party in parties:
    if party == 'independent':
        print(party.title())
    else:
        print(party.upper())