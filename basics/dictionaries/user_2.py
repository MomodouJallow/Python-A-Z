# Make a list of dictionaries
user_o = {'username':'efermi','fName':'enrico','lName':'fermi'}
user_1 = {'username':'anyang', 'fName':'adama', 'lName':'nyang'}
user_2 = {'username':'hpotter', 'fName':'harry', 'lName':'potter'}

users = [user_o, user_1, user_2]

for user in users:
    if user['username'] == 'anyang':
        user['username'] = 'zil'
        user['fName'] = 'ara k-maa'
        user['lName'] = 'jatta'
    for k, v in user.items():
        print(f"\nKey: {k.title()}")
        print(f"Value: {v.title()}")
        