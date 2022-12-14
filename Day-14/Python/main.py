import sys

sys.setrecursionlimit(10**5)
SOURCE = (500, 0)
C, F, S = set(), set(), set()

xmin, xmax, ymin, ymax = SOURCE[0], SOURCE[0], SOURCE[1], SOURCE[1]
for line in sys.stdin:
    xys = []
    for xy in line.strip().split(' -> '):
        x, y = map(int, xy.split(','))
        xys.append((x, y))
    for p1, p2 in zip(xys, xys[1:]):
        (x1, y1), (x2, y2) = p1, p2
        xmin = min(xmin, x1, x2)
        xmax = max(xmax, x1, x2)
        ymin = min(ymin, y1, y2)
        ymax = max(ymax, y1, y2)
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                C.add((x1, y))
        else:
            for x in range(min(x1, x2), max(x1, x2)+1):
                C.add((x, y1))

def draw(p, xh=None, yh=None):
    m = []
    for y in range(ymin, ymax + 1):
        m.append(['.'] * (xmax - xmin + 1))
    for x, y in C:
        if xmin <= x <= xmax and ymin <= y <= ymax:
            m[y - ymin][x - xmin] = '#'
    for x, y in F:
        if xmin <= x <= xmax and ymin <= y <= ymax:
            m[y - ymin][x - xmin] = '|'
    for x, y in S:
        if xmin <= x <= xmax and ymin <= y <= ymax:
            m[y - ymin][x - xmin] = '~'
    if (xh, yh) != (None, None): # highlight, for debugging
        s = m[yh - ymin][xh - xmin]
        m[yh - ymin][xh - xmin] = f'\033[91m{s[5]}\033[0m'
    m[SOURCE[1]-ymin][SOURCE[0] - xmin] = '+'
    with open(p, 'w+') as f:
        for r in m:
            f.write(''.join(r)+'\n')

# buffer
xrange = xmax - xmin
xmin -= int(2.5*xrange) + 3
xmax += int(2.5*xrange) + 3

touch = False
def fill(x, y):
    global touch
    if touch: return
    if y == ymax: touch = True

    # add to flowing spots
    F.add((x, y))

    # if empty space and haven't been flowed by water, recurse
    if (x, y + 1) not in C and (x, y + 1) not in F and SOURCE[1] <= y <= ymax:
        fill(x, y + 1)

    if (x, y + 1) in C or (x, y + 1) in S:
        for d in [-1, 1]:
            if (x + d, y + 1) not in C and (x + d, y + 1) not in S:
                fill(x + d, y + 1)

    if all([(x + d, y + 1) in C or (x + d, y + 1) in S for d in [-1, 0, 1]]):
        S.add((x, y))

fill(*SOURCE)
S = set(filter(lambda p: ymin <= p[1] <= ymax, S))
draw('part1.txt')
print('Part 1:', len(S))

ymax += 2
F, S, touch = set(), set(), False
OFFSET = 1000
for x in range(xmin - OFFSET, xmax + 1 + OFFSET):
    C.add((x, ymax))
fill(*SOURCE)
draw('part2.txt')
S = set(filter(lambda p: ymin <= p[1] <= ymax, S))
print('Part 2:', len(S))