class Dice:
    min: int
    max: int
    sides: int
    layout: list
    column_min: list
    column_max: list

    def __init__(self, sides, min_value, max_value):
        self.sides = sides
        self.min = min_value
        self.max = max_value
        self.layout = [self.min] * self.sides
        self.column_min = [self.min] * self.sides
        self.column_max = [self.max] * self.sides
        self.calc_column_minimums()
        self.calc_column_maximums()
        self.reset()

    def __str__(self):
        return str(self.layout)

    def calc_column_maximums(self):
        c = 1
        d = 0
        t = 0
        for i in range(1, self.sides + 1):
            self.column_max[-i] = self.max - d
            t += 1
            if t >= c:
                t = 0
                c += 1
                d += 1
        self.column_max[0] = 1

    def calc_column_minimums(self):
        c = 1
        d = 0
        t = 0
        for i in range(0, self.sides):
            self.column_min[i] = self.min + d
            t += 1
            if t >= c:
                t = 0
                c += 1
                d += 1
        self.column_min[-1] = self.max

    def get_sum_of_sides(self):
        return sum(self.layout)

    def next(self):
        try:
            col = 1
            self.layout[-col] += 1
            while self.layout[-col] > self.column_max[-col]:
                col += 1
                self.layout[-col] += 1
            if col > 1:
                l = self.layout[-col]
                for i in range(col, 0, -1):
                    self.layout[-i] = l
            self.layout[-1] = self.max
            return True
        except IndexError:
            return False

    def get_max_for_column(self, col):
        pass

    def reset(self):
        self.layout = self.column_min.copy()


def check_pair(a: list, b: list):
    # return False
    d = {}
    for i in a:
        for j in b:
            t = i + j
            count = d.get(t, 0)
            d[t] = count + 1
    for k, v in d.items():
        if v != 12 - abs(13 - k):
            return False
    return True


d1 = Dice(12, 1, 14)
d2 = Dice(12, 1, 10)

d1_possibles = []
d1.reset()
for j in range(1, 10000000):
    d1_possibles.append((d1.get_sum_of_sides(), d1.layout.copy()))
    if not d1.next():
        break

d2_possibles = []
d2.reset()
for j in range(1, 10000000):
    d2_possibles.append((d2.get_sum_of_sides(), d2.layout.copy()))
    if not d2.next():
        break

print(len(d1_possibles))
print(len(d2_possibles))

print(check_pair([1,2,3,4,5,6,7,8,9,10,11,12],[1,2,3,4,5,6,7,8,9,10,11,12]))

d1_count = 0
solutions = []

for d1 in d1_possibles:

    d1_len = len(d1_possibles)
    d1_count += 1
    print(f"{d1_count*100/d1_len} %")
    x = 156 - d1[0]

    d2_consider = (d2 for d2 in d2_possibles if d2[0] == x)

    for d2 in d2_consider:
        chk = check_pair(d1[1], d2[1])
        if chk:
            print(d1)
            print(d2)
            solutions.append((d1,d2))

for s in solutions:
    print("sol")
    print(s[0])
    print(s[1])

print("found")
print(len(solutions))