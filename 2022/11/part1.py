class Monkey():
    def __init__(self, lines):
        self.id = int(lines[0][7:8])
        self.items = []
        for x in lines[1][18:].split(","): self.items.append(int(x))
        self.operation = lines[2][13:]
        self.test = int(lines[3][21:])
        self.testTrue = int(lines[4][29:])
        self.testFalse = int(lines[5][30:])
        self.inspections = 0

    def __repr__(self):
        return f'[{self.id}, {self.items}, {self.operation}, {self.test}, {self.testTrue}, {self.testFalse}, {self.inspections}]'

            
monkeys = []
lines = open("input.txt", "r").read().splitlines()
for i in range(0,8):
    monkeys.append(Monkey(lines[(7*i):7*i+6]))

from pprint import pprint
pprint(monkeys)

new = 0 # to remove warning
for i in range(0, 20):
    for m in monkeys:
        for old in m.items:
            exec(m.operation) # new = old * 17, for example
            new = int(new/3)
            k = m.testTrue if new % m.test == 0 else m.testFalse
            # print(f'monkey {m.id} throws {new} to monkey {k}')
            monkeys[k].items.append(new)
            m.inspections += 1
        m.items = []

mm = sorted(monkeys, key=lambda x: x.inspections, reverse=True)
pprint(mm)
print(f'monkey business: {mm[0].inspections*mm[1].inspections}')