current_users = ['james', 'bob', 'dylan', 'admin', 'tay']
new_users = ['unicorn', 'bob', 'hippo', 'admin', 'man']

for user in new_users:
    if user in current_users:
        print(f'user name {user} is already taken')
    else:
        print(f'user {user} name is available')