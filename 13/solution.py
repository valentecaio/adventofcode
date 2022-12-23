import json

lines = open("input.txt").read().strip().splitlines()
lines[:] = (json.loads(x) for x in lines if x != '') # remove empty lines

NEXT = -1 # flag to compare next element
def compare(l, r):
    # print(f'compare l={l} r={r}')
    if isinstance(l, list) and isinstance(r, list):
        if len(l) == 0 and len(r) == 0:
            return NEXT
        elif len(l) == 0 and len(r) > 0:
            return True
        elif len(l) > 0 and len(r) == 0:
            return False
        else: # len(l) != 0 and len(r) != 0
            for i in range(0, min(len(l), len(r))):
                results = compare(l[i], r[i])
                if results != NEXT:
                    return results
            # if it got here, the existing elements in lists are equal
            if len(l) == len(r):
                return NEXT
            else:
                return len(l) < len(r)
    elif isinstance(l, int) and isinstance(r, int):
        if l == r:
            return NEXT
        else:
            return l < r
    elif isinstance(l, int): # r is list
        return compare([l], r)
    else: # l is list, r is int
        return compare(l, [r])

########## part 1 ##########
sum = 0
for k in range(0, len(lines), 2):
    if compare(lines[k], lines[k+1]):
        sum += k/2+1
print('part 1 solution:', int(sum))

########## part 2 ##########
def selectionSort(array):
    for step in range(len(array)):
        min_idx = step
        for i in range(step + 1, len(array)):
            # select the minimum element in each loop
            if compare(array[i], array[min_idx]):
                min_idx = i
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

lines += [[[2]], [[6]]]
selectionSort(lines)
print('part 2 solution:', (1+lines.index([[6]])) * (1+lines.index([[2]])))
