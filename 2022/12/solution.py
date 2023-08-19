
class P():
    def __init__(self, i, j):
        self.i, self.j = i, j

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

    def __repr__(self):
        return f'[{self.i},{self.j}]'


# helper
def printm(m):
    print('------------')
    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            print(f'{m[i][j]} ', end = '')
        print()


FLAG = 999

m = [list(x) for x in open("input.txt").read().strip().splitlines()]
print(f'm is {len(m)}x{len(m[0])}')

n = []
for _ in range(len(m)):
    n.append([FLAG] * len(m[0]))

for i in range(0, len(m)):
    for j in range(0, len(m[0])):
        m[i][j] = ord(m[i][j])
        if m[i][j] == ord('S'):
            start = P(i,j)
        elif m[i][j] == ord('E'):
            end = P(i,j)

m[start.i][start.j] = ord('a')
m[end.i][end.j] = ord('z')

n[end.i][end.j] = 0

print('start:', start)
print('end:  ', end)

queue = [end]
while len(queue) > 0:
    r = queue.pop()

    valid_neighbors = []
    # up
    s = P(r.i-1, r.j)
    if s.i>=0 and (n[s.i][s.j] == FLAG) and (m[s.i][s.j] >= m[r.i][r.j] -1):
        valid_neighbors.append(s)
    # down
    s = P(r.i+1, r.j)
    if s.i<len(m) and (n[s.i][s.j] == FLAG) and (m[s.i][s.j] >= m[r.i][r.j] -1):
        valid_neighbors.append(s)
    # right
    s = P(r.i, r.j+1)
    if s.j<len(m[0]) and (n[s.i][s.j] == FLAG) and (m[s.i][s.j] >= m[r.i][r.j] -1):
        valid_neighbors.append(s)
    # left
    s = P(r.i, r.j-1)
    if s.j>=0 and (n[s.i][s.j] == FLAG) and (m[s.i][s.j] >= m[r.i][r.j] -1):
        valid_neighbors.append(s)

    # printm(n)
    for s in valid_neighbors:
        n[s.i][s.j] = n[r.i][r.j] + 1
        queue.insert(0, s)

# printm(m)
# printm(n)
print('part 1 solution: ', n[start.i][start.j])

points_a = []
for i in range(0, len(m)):
    for j in range(0, len(m[0])):
        if m[i][j] == ord('a'):
            points_a.append(P(i,j))

distances = []
for p in points_a:
    distances.append(n[p.i][p.j])

print('part 2 solution: ', min(distances))
