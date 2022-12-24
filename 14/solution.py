
class Point():
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __repr__(self):
        return f'[{self.x},{self.y}]'


# helper
def printm(m):
    print('------------')
    for i in range(0, len(m)):
        for j in range(0, XMAX_PRINT):
            print(f'{m[i][j]} ', end = '')
        print()


# magic numbers for the given input
XMAX_PRINT = 80
XMAX = 500
YMAX = 190
XOFFSET = 460

lines = [x.split(' -> ') for x in open("input.txt").read().strip().splitlines()]
m = [['.' for _ in range(XMAX)] for _ in range(YMAX)]

origin = Point(500-XOFFSET, 0)
m[origin.y][origin.x] = '+'
biggest_y = 0

for line in lines:
    points = []
    for elem in line:
        x, y = elem.split(',')
        points.append(Point(int(x)-XOFFSET, int(y)))
        biggest_y = max(biggest_y, int(y))
    for i in range(len(points)-1):
        p1, p2 = points[i:i+2]
        # draw line from p1 to p2
        for dx in range(min(p1.x, p2.x), max(p1.x, p2.x)+1):
            m[p1.y][dx] = '#'
        for dy in range(min(p1.y, p2.y), max(p1.y, p2.y)+1):
            m[dy][p1.x] = '#'


########## part 1 ##########
i = 0
run = True
while run:
    sand = Point(origin.x, origin.y)
    while True:
        if sand.y+1 >= YMAX:
            run = False
            break
        if m[sand.y+1][sand.x] == '.':
            sand.y += 1
        elif m[sand.y+1][sand.x-1] == '.':
            sand.y += 1
            sand.x -= 1
        elif m[sand.y+1][sand.x+1] == '.':
            sand.y += 1
            sand.x += 1
        else:
            m[sand.y][sand.x] = 'o'
            i+= 1
            break
printm(m)


########## part 2 ##########
j = i
run = True
while run:
    j += 1
    sand = Point(origin.x, origin.y)
    while True:
        if sand.y+1 >= biggest_y+2:
            m[sand.y][sand.x] = 'o'
            break
        if m[sand.y+1][sand.x] == '.':
            sand.y += 1
        elif m[sand.y+1][sand.x-1] == '.':
            sand.y += 1
            sand.x -= 1
        elif m[sand.y+1][sand.x+1] == '.':
            sand.y += 1
            sand.x += 1
        else:
            if sand == origin:
                run = False
            m[sand.y][sand.x] = 'o'
            break
printm(m)

print('part 1 solution:', i)
print('part 2 solution:', j)
