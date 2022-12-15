import sys, re
from z3 import *

sb = {}
xmin = ymin = float('inf')
xmax = ymax = -float('inf')
for line in sys.stdin:
    res = re.findall('Sensor at x=([-\d]+), y=([-\d]+): closest beacon is at x=([-\d]+), y=([-\d]+)', line)[0]
    xs, ys, xb, yb = map(int, res)
    sb[(xs, ys)] = (xb, yb)
    xmin = min(xmin, xs, xb)
    xmax = max(xmax, xs, xb)
    ymin = min(ymin, ys, yb)
    ymax = max(ymax, ys, yb)

S = set(sb.keys())
B = set(sb.values())
C = {}
for x, y in S:
    if y not in C:
        C[y] = set()
    C[y].add(x)

# buffer
xmin -= 3
ymin -= 3
xmax += 3
ymax += 3
xrange = xmax - xmin
yrange = ymax - ymin

def draw():
    m = []
    for y in range(ymin, ymax + 1):
        m.append(['.'] * (xmax - xmin + 1))
    for y in C:
        for x in C[y]:
            if xmin <= x <= xmax and ymin <= y <= ymax:
                m[y - ymin][x - xmin] = '#'
    for x, y in S:
        if xmin <= x <= xmax and ymin <= y <= ymax:
            m[y - ymin][x - xmin] = 'S'
    for x, y in B:
        if xmin <= x <= xmax and ymin <= y <= ymax:
            m[y - ymin][x - xmin] = 'B'
    for r in m:
        print(''.join(r))

md, mmd =  {}, 0
for (xs, ys), (xb, yb) in sb.items():
    md[(xs, ys)] = abs(xs - xb) + abs(ys - yb)
    mmd = max(mmd, md[(xs, ys)])

# I didn't merge interval because lazy :)
# Yes it's longer
def part1():
    Y = 2_000_000
    c = -len({x for x, y in B if y == Y})
    for x in range(xmin - mmd, xmax + mmd):
        for xs, ys in S:
            if abs(xs - x) + abs(ys - Y) <= md[(xs, ys)]:
                c += 1
                break
    print('Part 1:', c)

def part2():
    def z3_abs(x):
        return If(x >= 0, x, -x)
    x, y, s = Int('x'), Int('y'), Solver()
    LIM = 4_000_000
    args = [x <= LIM, x >= 0, y <= LIM, y >= 0] + [z3_abs(xs - x) + z3_abs(ys - y) > md[(xs, ys)] for xs, ys in S]
    for arg in args:
        s.add(arg)
    assert s.check() == sat
    print('Part 2:', eval(str(LIM*s.model()[x] + s.model()[y])))

part1()
part2()