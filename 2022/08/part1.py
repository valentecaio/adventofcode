def is_visible(m, i, j):
    visible_up = visible_down = visible_left = visible_right = True
    for k in range(0, i):
        if m[k][j] >= m[i][j]:
            visible_up = False
            break
    for k in range(i+1, len(m)):
        if m[k][j] >= m[i][j]:
            visible_down = False
            break
    for k in range(0, j):
        if m[i][k] >= m[i][j]:
            visible_left = False
            break
    for k in range(j+1, len(m[0])):
        if m[i][k] >= m[i][j]:
            visible_right = False
            break
    return visible_up or visible_down or visible_left or visible_right

m = []
for line in open("input.txt", "r").readlines():
    m.append(list(line[:-1]))
print(f'm is {len(m)}x{len(m[0])}')

sum=0
for i in range(0,len(m)):
    for j in range(0, len(m[0])):
        if is_visible(m, i, j):
            sum += 1
print(f'there are {sum} visible elements')