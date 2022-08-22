n = int(input('Input year: '))
if(((n % 4 == 0) and (n % 100 > 0))) | (n % 400 == 0):
    print('True')
else:
    print('False')