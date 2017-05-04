from Prac07.pointClass import Point
import random

def main():
    points = [Point(2, 2), Point(4, 4), Point(6, 6)]
    for point in points:
        print(point, end=' ')
    print()

    i = random.randint(0,10)
    for point in points:
        point.move(i, i)
        i = random.randint(0,10)

    for point in points:
        print(point, end=' ')

    print()


main()
