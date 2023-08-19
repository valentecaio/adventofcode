def scenic(m, i, j):
    up = down = left = right = 0
    for x in range(i-1, -1, -1):
        up += 1
        if m[x][j] >= m[i][j]:
            break
    for x in range(i+1, len(m)):
        down += 1
        if m[x][j] >= m[i][j]:
            break
    for x in range(j-1, -1, -1):
        left += 1
        if m[i][x] >= m[i][j]:
            break
    for x in range(j+1, len(m[0])):
        right += 1
        if m[i][x] >= m[i][j]:
            break
    return up*down*right*left

m = []
for line in open("input.txt", "r").readlines():
    m.append(list(line[:-1]))
print(f'm is {len(m)}x{len(m[0])}')

scenics = []
for i in range(0,len(m)):
    for j in range(0, len(m[0])):
        scenics.append(scenic(m, i, j))
print(f'the biggest scenic score is {max(scenics)}')