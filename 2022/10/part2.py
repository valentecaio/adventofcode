lines = (line.strip() for line in open("input.txt", "r").readlines())
x = cycle = 1
history = []
for l in lines:
    if l[:4] == "addx":
       history.append(x)
       history.append(x)
       x += int(l[5:])
       cycle += 2
    else:
        history.append(x)
        cycle += 1

cycle = 0
for x in history:
    if cycle >= 40:
        cycle = 0
        print()
    c = '#' if cycle in [x-1, x, x+1] else '.'
    print(c, end = '')
    cycle += 1
