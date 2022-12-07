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

    def __lt__(self, other):
        return self.size < other.size


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


# create list of all dirs and sort by size
ls_dirs = []
def tree_to_list(node):
    if node.is_dir:
        ls_dirs.append(node)
        for child in node.children:
            tree_to_list(child)
tree_to_list(root)
ls_dirs.sort()


# list dirs
print("\n\nDIRECTORIES:\n")
for dir in ls_dirs:
    print(f'{dir.name: <{15}} {dir.size}')


needed_space = ls_dirs[-1].size + 30000000 - 70000000
print(f'\nneeded space is {needed_space}')
for dir in ls_dirs:
    if dir.size > needed_space:
        print(f'\nfinal answer: delete dir {dir.name} (size {dir.size})')
        break
