#посчитаем факториал числа

def fak(number):
    if number <= 1 and number == 0:
        return 1
    elif number < 0:
        return 'Вы ввели говно' 
    else:
        return number*fak(number - 1)

print(fak(-1))

