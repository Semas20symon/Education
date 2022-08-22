import random
count = 10

while count>0:
    print('Attemt left: ', count)
    user_num = int(input('Введите число от 1 до 10: '))
    some_random = random.randint(1, 10)
    print('Random number is: ', some_random)
    if some_random == user_num:
        print('You won')
        exit( )
    else:
        print('You lose')
    count-=1
