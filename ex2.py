import pygame as pg
import numpy as np
import random
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
N = 5

# Read input file
total = 0
allNums = []
with open(sys.argv[1], 'r') as lines:
    data = lines.readlines()
    for line in data:
        allNums += line.strip().split(" ")
    for num in allNums:
        total += int(num)
total = total / 2
print(total)

pg.init()
screenSize = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pg.display.set_mode(screenSize)
pg.display.set_caption("Griddlers")
screen.fill(WHITE)
pg.display.flip()


def split_list(a_list):
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]


def generate_solution():
    numbers = [0, 1]
    size = len(data)
    keys = []
    for i in range(N):
        keys.append(i)
    lst = []
    final = []
    for index in data:
        new = index.strip().split(" ")
        final.append(new)

    first, second = split_list(final)
    for i, v in enumerate(first):
        lst.append([i, [int(value) for value in v]])
    print(lst)
    print(lst[3][1][0])
    solution = [[np.random.choice(numbers) for y in range(N)] for x in range(N)]
    return solution


def drawGrid(func_matrix):
    blockSize = 10  # Set the size of the grid block
    i = 0  # Rows of matrix
    j = 0  # Columns of matrix
    for y in range(3, WINDOW_WIDTH, blockSize + 3):
        for x in range(3, WINDOW_HEIGHT, blockSize + 3):
            rect = pg.Rect(x, y, blockSize, blockSize)
            try:
                if func_matrix[i][j] == 0:
                    pg.draw.rect(screen, WHITE, rect)
                    pg.display.flip()
                elif func_matrix[i][j] == 1:
                    pg.draw.rect(screen, BLACK, rect)
                    pg.display.flip()
            except:
                pg.draw.rect(screen, WHITE, rect)

            j = j + 1
        j = 0
        i = i + 1


if __name__ == '__main__':
    generate_solution()
    numbers = [0, 1]
    matrix = [[np.random.choice(numbers) for y in range(N)] for x in range(N)]
    finish = False
    while not finish:
        # drawGrid(matrix)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                finish = True
    pg.quit()
