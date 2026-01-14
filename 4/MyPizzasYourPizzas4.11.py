pizza_list = ['margarita', 'pesto chicken', 'marinara']

for pizza in pizza_list:
    print(f'I like {pizza.title()}')

print('I really love pizza!')

friend_pizzas = pizza_list[:]

pizza_list.append('salty dog')
friend_pizzas.append('hawian')

print('---My-favorite-pizzas-are---')
for myPizza in pizza_list:
    print(f'{myPizza.title()}')

print('----------------------------')

print('\n---my-friends-favorite-pizzas-are---')
for friend in friend_pizzas:
    print(f'{friend.title()}')

print('------------------------------------')
