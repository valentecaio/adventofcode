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
print(history)
tot = sum(k*history[k-1] for k in [20, 60, 100, 140, 180, 220])
print(tot)