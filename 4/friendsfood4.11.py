my_foods = ['pizza', 'falafel', 'carrot cake']

# make friends foods just points to my foods so its a refrence.
# thats why its better to do it as a slice [:] if we dont want the refrence variable to just be a pointer
# friend_foods = my_foods[:]

friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(f'\n my fav foods are {my_foods}')
print(f'\n my firends fav foods are {friend_foods}')
print('----------MY-FOOD-------------------')
for food in my_foods:
    print(f'{food.title()}')
print('------------------------------------')
print('\n---------MY-FRIENDS-FOOD------------')
for friend in friend_foods:
    print(f'{friend.title()}')
print('--------------------------------------')
