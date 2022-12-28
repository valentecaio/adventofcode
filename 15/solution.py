import re
from pprint import pprint

class Sensor():
    def __init__(self, x, y, range):
        self.x, self.y, self.range = x, y, range

    def __repr__(self):
        return f'[{self.x},{self.y},{self.range}]'


def manhattan(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

########## input ##########
lines = open("input.txt").read().strip().splitlines()
sensors = []
occupied = []
min_x = max_x = 0
for l in lines:
    r = re.match(r"Sensor at x=(?P<sx>[-+]?\d+), y=(?P<sy>[-+]?\d+): closest beacon is at x=(?P<bx>[-+]?\d+), y=(?P<by>[-+]?\d+)", l)
    sx, sy, bx, by = int(r['sx']), int(r['sy']), int(r['bx']), int(r['by'])
    sensors.append(Sensor(sx, sy, manhattan(sx, sy, bx, by)))
    occupied.append((sx, sy))
    occupied.append((bx, by))
    min_x = min(sx, bx, min_x)
    max_x = max(sx, bx, max_x)
pprint(sensors)

occupied = list(dict.fromkeys(occupied))
occupied.sort()
print('occupied:', occupied)

########## part 1 ##########
print(f'min_x={min_x}, max_x={max_x}')
y = 2000000
sum = 0
for x in range(min_x, max_x+1):
    # skip occupied points
    if (x,y) in occupied:
        continue
    for s in sensors:
        if s.range >= manhattan(x, y, s.x, s.y):
            sum += 1
            break
print("part 1 solution:", sum)

########## part 2 ##########
end = 4_000_000
for y in range(end+1):
    x=0
    while x < end:
        if (x,y) in occupied:
            x += 1
            continue
        not_in_range_of_any_sensor = True
        for s in sensors:
            dx = s.range - abs(y-s.y)
            minx, maxx = s.x-dx, s.x+dx
            if x >= minx and x <= maxx:
                not_in_range_of_any_sensor = False
                x = maxx+1
        if not_in_range_of_any_sensor:
            print(f'part 2 solution: {x*end+y} (found x={x}, y={y})')
            exit()
