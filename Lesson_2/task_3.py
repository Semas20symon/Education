speed = int(input('Введите скорость: '))
time = int(input('Введите время: '))
distance = (speed * time) % 100
print('Вася остановился на',(distance), 'отметке')
