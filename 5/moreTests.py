pizza_list = ['margarita', 'pesto chicken', 'marinara', 'bbq chicken', 'pepperoni', 'Hawaiian']

for pizza in pizza_list:
    if pizza == 'bbq chicken':
        print(f'BBQ chicken pizza is average af')
        
for pizza_type in pizza_list:
    if pizza_type.lower() == 'hawaiian':
        print('I mean its all right')

if 'chicken kebab' not in pizza_list:
    print('perfect a chicken kebab is not ment to be in the pizza list...')

man = 'man'
woman = 'woman'

if woman != man:
    print('yup woman is not man so correct')

if 'MAN'.lower() == man:
    print('yes sir the lower function works on just a string inside of the condition.')

if 30 == 30:
    print('yup your math is mathing')

if 30 != 31:
    print('yup your logic is mathing')

if 30 == 30 and 'Man'.lower() == man:
    print('yes you have a receeding hairline')

if man == woman or woman == woman:
    print("yup a woman is a woman.")
