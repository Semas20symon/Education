list_of_six = []
for elements in range(100, 197, 6):
    list_of_six.append(elements)
    print('Список:', list_of_six)
for num in list_of_six:
    if (num % 5) == 0 and num <= 150:
        print('Числа из списка которые делятся на 5 без остатка и не больше 150: ', num)


