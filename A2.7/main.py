# Type TEST to run the test function
# FourSquare is the manually typed command file and RepeatFS makes use of the REPEAT command

from matplotlib import pyplot as plt
from math import *


def forward_function(pen_tuple, distance):
    previous_x = float(pen_tuple[0])
    previous_y = float(pen_tuple[1])
    angle_rad = radians(float(pen_tuple[3]))
    a = previous_x + float(distance) * sin(angle_rad)
    b = previous_y + float(distance) * cos(angle_rad)
    c = pen_tuple[2]
    d = pen_tuple[3]
    pen = (a, b, c, d)
    x = [previous_x, a]
    y = [previous_y, b]
    if c:
        plt.plot(previous_x, previous_y)
        plt.plot(x, y, 'r-')

    return pen


def rotation_function(pen_tuple, direction):
    a = pen_tuple[0]
    b = pen_tuple[1]
    c = pen_tuple[2]
    d = float(pen_tuple[3]) + float(direction)
    pen = (a, b, c, d)
    return pen


def pen_function(pen_tuple, contact):
    a = pen_tuple[0]
    b = pen_tuple[1]
    c = pen_tuple[2]
    d = pen_tuple[3]
    if contact == 'DOWN':
        c = True
    else:
        c = False
    pen = (a, b, c, d)

    return pen


def test():
    plt.axis([-400, 400, -400, 400])
    pen = (-100, 0, False, 0)
    pen_v1 = 'DOWN'
    forward_v1 = '100'
    rotate_v1 = '135'
    pen = pen_function(pen, pen_v1)
    pen = rotation_function(pen, rotate_v1)
    pen = forward_function(pen, forward_v1)
    rotate_v2 = '270'
    forward_v2 = '250'
    pen = rotation_function(pen, rotate_v2)
    forward_function(pen, forward_v2)
    plt.show()
    print('Test Complete')
    exit(1)


def main():
    filename = input()
    if filename.find('TEST') > -1:
        test()
    plt.axis([-400, 400, -400, 400])
    pen = (0, 0, False, 0)
    # pen = (x,y,state,angle)
    file = open(filename, 'r')
    file_l = file.readlines()

    for i in range(len(file_l)):
        entry = file_l[i]

        if entry.find('FORWARD') > -1:
            split = entry.split()
            value = split[1]
            pen = forward_function(pen, value)

        elif entry.find('ROTATE') > -1:
            split = entry.split()
            value = split[1]
            pen = rotation_function(pen, value)

        elif entry.find('PEN') > -1:
            split = entry.split()
            value = split[1]
            pen = pen_function(pen, value)

# This is the repeat command code, it checks for the keyword REPEAT and determines if it has found the beginning or the
# end. Commands between repeats are stored in a separate list and looped over as many times as the argument states.

        elif entry == 'REPEAT END\n' or entry == 'REPEAT END':
            continue

        elif entry.find('REPEAT') > -1:
            pos = i
            split = entry.split()
            value = split[1]
            for j in range(int(value)):
                y =[]
                for k in file_l[pos+1::]:
                    if k == 'REPEAT END\n' or k == 'REPEAT END':
                        break
                    else:
                        y.append(k)

                for m in range(len(y)):
                    entry2 = y[m]
                    if entry2.find('FORWARD') > -1:
                        split2 = entry2.split()
                        value2 = split2[1]
                        pen = forward_function(pen, value2)
                    elif entry2.find('ROTATE') > -1:
                        split2 = entry2.split()
                        value2 = split2[1]
                        pen = rotation_function(pen, value2)
                    elif entry2.find('PEN') > -1:
                        split2 = entry2.split()
                        value2 = split2[1]
                        pen = pen_function(pen, value2)

    plt.show()


main()

