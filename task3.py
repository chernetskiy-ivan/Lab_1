import numpy as np
import random

size = 15
matrix = np.zeros((size, size), dtype='int64')
stack_current_move = []
matrix[1][2] = 1
matrix[1][14] = 1
matrix[5][14] = 1
matrix[5][8] = 1
matrix[7][2] = 1
matrix[7][4] = 1
matrix[11][4] = 1
matrix[11][8] = 1

def search_start(array):
    [x, y] = random.randint(0, size - 1), random.randint(0, size - 1)
    while array[x][y] != 1:
        [x, y] = random.randint(0, size - 1), random.randint(0, size - 1)
    return x, y


class Cell:
    def __init__(self, value):
        self.routes = {'DOWN': False, 'UP': False, 'RIGHT': False, 'LEFT': False}
        self.visited = False
        self.value = value


stack = [search_start(matrix)]

print("stack[0] ", stack[0])


class Field:
    i = 0
    #распаковываем кортеж
    x_start, y_start = stack[0]
    x_current, y_current = x_start, y_start

    def __init__(self, array):
        self.field = []
        for m in range(size):
            a = []
            for n in range(size):
                a.append(Cell(array[m][n]))
            self.field.append(a)


def search():
    work_field = Field(matrix)
    work_field.field[Field.x_start][Field.y_start].visited = True
    while Field.i != -1:
        exist = False
        Field.x_current, Field.y_current = stack[Field.i]
        #идем вниз 
        while 0 <= Field.x_current < 14:
            Field.x_current += 1
            if work_field.field[Field.x_current][Field.y_current].value == 1:
                stack_current_move.append((Field.x_current, Field.y_current))
                exist = True
                break
        Field.x_current, Field.y_current = stack[Field.i]
        if not exist:
            stack_current_move.append((-1, -1))
        else:
            exist = False

        #идем вверх
        while 0 < Field.x_current <= 14:
            Field.x_current -= 1
            if work_field.field[Field.x_current][Field.y_current].value == 1:
                stack_current_move.append((Field.x_current, Field.y_current))
                exist = True
                break
        Field.x_current, Field.y_current = stack[Field.i]
        if not exist:
            stack_current_move.append((-1, -1))
        else:
            exist = False

        #идем вправо
        while 0 <= Field.y_current < 14:
            Field.y_current += 1
            if work_field.field[Field.x_current][Field.y_current].value == 1:
                stack_current_move.append((Field.x_current, Field.y_current))
                exist = True
                break
        Field.x_current, Field.y_current = stack[Field.i]
        if not exist:
            stack_current_move.append((-1, -1))
        else:
            exist = False

        #идем влево
        while 0 < Field.y_current <= 14:
            Field.y_current -= 1
            if work_field.field[Field.x_current][Field.y_current].value == 1:
                stack_current_move.append((Field.x_current, Field.y_current))
                exist = True
                break
        Field.x_current, Field.y_current = stack[Field.i]
        if not exist:
            stack_current_move.append((-1, -1))

        for c in range(len(stack_current_move)):
            x_current, y_current = stack_current_move[c]
            if stack_current_move[c] != (-1, -1):
                if work_field.field[Field.x_current][Field.y_current].routes['DOWN'] and c == 1:
                    continue
                elif work_field.field[Field.x_current][Field.y_current].routes['UP'] and c == 0:
                    continue
                elif work_field.field[Field.x_current][Field.y_current].routes['RIGHT'] and c == 3:
                    continue
                elif work_field.field[Field.x_current][Field.y_current].routes['LEFT'] and c == 2:
                    continue
                if work_field.field[x_current][y_current].visited:
                    stack.append((x_current, y_current))
                    Field.i = -1
                    break
                else:
                    if c == 0:
                        work_field.field[x_current][y_current].routes['DOWN'] = True
                    elif c == 1:
                        work_field.field[x_current][y_current].routes['UP'] = True
                    elif c == 2:
                        work_field.field[x_current][y_current].routes['RIGHT'] = True
                    elif c == 3:
                        work_field.field[x_current][y_current].routes['LEFT'] = True

                stack.append(stack_current_move[c])
                Field.i += 1
                stack_current_move.clear()
                work_field.field[x_current][y_current].visited = True
                break


search()
for n in range(len(stack)):
    if n == len(stack) - 1:
        print(format(stack[n]), end=' ')
        break
    print('{}->'.format(stack[n]), end=' ')