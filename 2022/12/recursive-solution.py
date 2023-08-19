# this is a valid solution for a small matrix (the example matrix)
# will run forever for a big matrix (day 12 input is too big)

class P():
    def __init__(self, i, j):
        self.i, self.j = i, j

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

    def __lt__(self, other):
        return m[self.i][self.j] < m[other.i][other.j]

    def __repr__(self):
        return f'[{self.i},{self.j}]'


m = []
for line in open("input.txt", "r").readlines():
    r = []
    for c in line[:-1]:
        r.append(ord(c))
    m.append(r)
print(f'm is {len(m)}x{len(m[0])}')


for i in range(0, len(m)):
    for j in range(0, len(m[0])):
        if m[i][j] == ord('S'):
            r = P(i,j)
        elif m[i][j] == ord('E'):
            end = P(i,j)

m[r.i][r.j] = ord('a')
m[end.i][end.j] = ord('z')+1

# def printm():
#     for i in range(0, len(m)):
#         for j in range(0, len(m[0])):
#             print(f'{m[i][j]} ', end = '')
#         print()
# printm()

print(r)
print(end)

solutions = []
def rec_find_paths(path):
    r = path[-1]
    # print(f'rec_find_paths() r={r} path={path}')

    # end
    if r == end:
        print(f'FOUND NEW SOLUTION path={path}')
        solutions.append(path)
        return

    valid_neighbors = []

    # up
    s = P(r.i-1, r.j)
    if s.i>=0 and (m[s.i][s.j] <= m[r.i][r.j] +1) and s not in path:
        valid_neighbors.append(s)
    # down
    s = P(r.i+1, r.j)
    if s.i<len(m) and (m[s.i][s.j] <= m[r.i][r.j] +1) and s not in path:
        valid_neighbors.append(s)
    # right
    s = P(r.i, r.j+1)
    if s.j<len(m[0]) and (m[s.i][s.j] <= m[r.i][r.j] +1) and s not in path:
        valid_neighbors.append(s)
    # left
    s = P(r.i, r.j-1)
    if s.j>=0 and (m[s.i][s.j] <= m[r.i][r.j] +1) and s not in path:
        valid_neighbors.append(s)

    # heuristic
    valid_neighbors.sort(reverse=True)
    for s in valid_neighbors:
        newpath = path[:]
        newpath.append(s)
        rec_find_paths(newpath)


rec_find_paths([r])

# from pprint import pprint
# pprint(solutions)
lens = []
for s in solutions:
    lens.append(len(s)-1)
print(lens)
print(min(lens))
