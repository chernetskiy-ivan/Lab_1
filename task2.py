from consts_for_task2 import *
import math

def location(area):
    #в данной функции случайно раставляем вышки и запоминаем их координаты
    position = random.randint(0, size - 1), random.randint(0, size - 1)

    #pos of towers with power1
    for i in range(5):
        while area[position] != 0:
            position = random.randint(0, size - 1), random.randint(0, size - 1)
        towers_area[position] = power1
        towers[i] = position
    #pos of towers with power2
    for i in range(3):
        while area[position] != 0:
            position = random.randint(0, size - 1), random.randint(0, size - 1)
        towers_area[position] = power2
        towers[5 + i] = position
    #pos of towers with power3
    for i in range(2):
        while area[position] != 0:
            position = random.randint(0, size - 1), random.randint(0, size - 1)
        towers_area[position] = power3
        towers[8 + i] = position

def signal(signal_area, density):
    #Посчитали и запомнили позиции где связь лучше 1
    amount_of_good_connection = 0
    population = 0
    signal_area_point = np.zeros(10)
    for i in range(size):
        for j in range(size):
            population += density[i][j]
            for k in range(10):
                if i == towers[k][0] and j == towers[k][1]:
                    signal_area_point[k] = towers_area[i][j]
                    continue
                elif k <= 4:
                    signal_area_point[k] = power1 / ((i - towers[k, 0]) ** 2 + (j - towers[k, 1]) ** 2)
                elif 5 <= k <= 7:
                    signal_area_point[k] = power2 / ((i - towers[k, 0]) ** 2 + (j - towers[k, 1]) ** 2)
                elif 8 <= k <= 9:
                    signal_area_point[k] = power3 / ((i - towers[k, 0]) ** 2 + (j - towers[k, 1]) ** 2)
            signal_area[i][j] = max(signal_area_point)
            if signal_area[i][j] >= 1:
                amount_of_good_connection += density[i][j]
                x.append(j)
                y.append(i)
    return amount_of_good_connection, population


if __name__ == "__main__":
    location(towers_area)
    a = signal(signal_level, density)
    print('Людей с сигналом >=1: {}, всего людей {}'.format(a[0], a[1]))
    print('Хорошая связь у ',math.ceil((a[0]/a[1])*100),'%  населения')

    #распаковываю кортеж
    figure, ax = plt.subplots()
    figure.set_size_inches(8, 4)

    ax.imshow(signal_level, cmap=gradient_color, origin='lower', vmin=0, vmax=power3)
    plt.show()
