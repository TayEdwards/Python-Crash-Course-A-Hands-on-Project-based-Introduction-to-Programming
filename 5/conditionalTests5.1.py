#5 true
age = 30

print('Next 5 statement will be true')
if age == 30:
    print('correct this statement is true_s1')

if age >= 30:
    print('correct this statement is true_s2')

if age > 0:
    print('correct this statement is true_s3')

#what is my purpose, to put butter on my toast.
if age == 30 or True == True:
    print('correct this statement is true_s4')

if age < 31 and True == True:
    print('correct this statement is true_s5')

#5 false

print('--Next 5 statement will be false--')
if age != 30:
    print('this shouldnt print_s1')

if age < 30:
    print('this shouldnt print_s2')

if age == 1:
    print('this shouldnt print_s3')

if age == 31 or True == False:
    print('this shouldnt print_s4')

if age > 31:
    print('this shouldnt print_s5')

print('--None of these statements printed--')