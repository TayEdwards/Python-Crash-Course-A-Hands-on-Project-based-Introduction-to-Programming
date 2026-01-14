usernames = ['james', 'bob', 'dylan', 'admin', 'tay']

# quite interesting using the if statement here of the list is a check to see
# if the list is empty.
if usernames:
    for user in usernames:
        print(f'Welcome {user}')
        if user.lower() == 'admin':
            print('Hello admin would you like to see a status report?')
        else:
            print('haha not even a super user!')
else:
    print('Nah the list is empty boss')
