
pizza_list = ['margarita', 'pesto chicken', 'marinara']

for pizza in pizza_list:
    print(f'I like {pizza.title()}')

print('I really love pizza!')


pizza_list_copy = pizza_list[:]
print(pizza_list_copy)
print()
print('-----syntax-----')
print('[start:stop:step]')
print('----------------')
print(pizza_list_copy[0:2])
print(pizza_list_copy[:2])
print(pizza_list_copy[-1:])
print(pizza_list_copy[0:3])