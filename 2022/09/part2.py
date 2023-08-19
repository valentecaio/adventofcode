class P():
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f'[{self.x},{self.y}]'

# used for tests
def printm(r):
    print("\n\n", "_"*50)
    for j in range(-10, 20):
        for i in range(-10, 20):
            c = "."
            for k in range(0, 10):
                if r[k].x==i and r[k].y==j:
                    c = k
                    break
            print(c, end = '')
        print("")
            

r = [] # rope
for i in range(0, 10): r.append(P(0,0))
visited = []
for l in (line.strip() for line in open("input.txt", "r").readlines()):
    for _ in range(0, int(l[2:])):
        if   l[0] == 'U': r[0].y += 1
        elif l[0] == 'D': r[0].y -= 1
        elif l[0] == 'L': r[0].x -= 1
        elif l[0] == 'R': r[0].x += 1
        for i in range(1, 10):
            dx, dy = abs(r[i-1].x - r[i].x), abs(r[i-1].y - r[i].y)
            if dx>1 and dy>1:
                r[i].x = int((r[i-1].x+r[i].x)/2)
                r[i].y = int((r[i-1].y+r[i].y)/2)
            elif dx>1:
                r[i].x = int((r[i-1].x+r[i].x)/2)
                r[i].y = r[i-1].y
            elif dy>1:
                r[i].y = int((r[i-1].y+r[i].y)/2)
                r[i].x = r[i-1].x
        visited.append((r[9].x, r[9].y))
        # printm(r)

print(len(list(dict.fromkeys(visited))))