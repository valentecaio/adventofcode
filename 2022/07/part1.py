class Node:
    def __init__(self, name, parent, is_dir, size=0):
        self.name = name
        self.parent = parent
        self.is_dir = is_dir
        self.size = size
        self.children = []

    def __str__(self, level=0):
        ret = f'{"  "*level}- {self.name}: {self.size}\n'
        for child in self.children:
            ret += child.__str__(level+1)
        return ret


# create tree
ptr = root = Node("/", None, True)
lines = (line.strip() for line in open("input.txt", "r").readlines()[1:])
for l in lines:
    if l == "$ ls":
        continue
    elif l == "$ cd ..":
        ptr = ptr.parent
    elif l.startswith("$ cd"):
        n = Node(l.split(" ")[2], ptr, True)
        ptr.children.append(n)
        ptr = n
    elif l.startswith("dir"):
        continue
    else: # l = "2309432 filename.txt"
        n = Node(l.split(" ")[1], ptr, False, int(l.split(" ")[0]))
        ptr.children.append(n)
# print(root)


# calculate dir sizes
def sum_sizes(node):
    if node.is_dir:
        for child in node.children:
            node.size += sum_sizes(child)
    return node.size
sum_sizes(root)
print(root)


# find small dirs
small_dirs = []
small_dir_threshold = 100000
def find_small_dirs(node):
    if node.is_dir:
        for child in node.children:
            find_small_dirs(child)
        if node.size < small_dir_threshold and node not in small_dirs:
            small_dirs.append(node)
find_small_dirs(root)


# sum small dirs
sum = 0
print("\n\nSMALL DIRS:\n")
for dir in small_dirs:
    print(f'{dir.name: <{15}} {dir.size}')
    sum += dir.size

print(f'\n\nfinal answer: {sum}')
