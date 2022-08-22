some_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
some_num = [1, 2, 3, 4, 5, 6, 7,  8]
print('''
Введите шахматный ход для вашего коня.
Важно вводите ход в формате настоящей игры!
Например: А2 - D7
И не забудь верхний регистр и англ. раскладку
''')
start = input('Начальная точка фигуры: ')
finish = input('Конечная точка фигуры: ')
start = list(start)
finish = list(finish)
x1 = 0
x2 = 0
y1 = int(start[1])
y2 = int(start[1])
for letter in some_letters:
    a = int(some_letters.index(letter))
    if start[0] == some_letters[a]:
        x1 = some_num[a]
    if finish[0] == some_letters[a]:
        x2 = some_num[a]

dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('Да конь может так ходить!')
else:
    print('Конь не может так ходить!')