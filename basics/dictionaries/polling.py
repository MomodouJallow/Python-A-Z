# Use the code in favorite_languages.py.
# Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }


pollers = ['harry', 'sarah', 'phil', 'bij', 'jen', 'edward', 'zil']
for poller in pollers:
    if poller in favorite_languages.keys():
        print(f"{poller.title()}, thank you for taking the poll.")
    else:
        print(f"{poller.title()}, please take your poll!")
        
