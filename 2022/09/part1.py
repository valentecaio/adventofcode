Hx = Hy = Tx = Ty = 0
track = []
visited = []
lines = (line.strip() for line in open("input.txt", "r").readlines())
for l in lines:
    for _ in range(0, int(l[2:])):
        if   l[0] == 'U': Hy += 1
        elif l[0] == 'D': Hy -= 1
        elif l[0] == 'L': Hx -= 1
        elif l[0] == 'R': Hx += 1
        if   abs(Hx-Tx) > 1: Ty, Tx = Hy, int((Hx+Tx)/2)
        elif abs(Hy-Ty) > 1: Tx, Ty = Hx, int((Hy+Ty)/2)
        visited.append((Tx, Ty))
        track.append((l[0], (Hx, Hy), (Tx, Ty), len(list(dict.fromkeys(visited)))))

from pprint import pprint
pprint(track)
print(f'answer: {len(list(dict.fromkeys(visited)))}')