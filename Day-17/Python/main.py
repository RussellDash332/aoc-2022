jetpack = input()

LENGTH = 7
HEIGHT = 0
def draw(print_rows=0):
    m = [['.' for _ in range(LENGTH)] for _ in range(HEIGHT + 2)]
    for x, y in D:
        m[len(m)-1-y][x] = '#'
    if print_rows:
        for r in m[:print_rows]:
            print(''.join(r))
        print()
    return m

tetrominos = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)]
]

D = set()
pos, t = 0, 0
def drop():
    global t, pos, D, HEIGHT
    tet = {(x+2, y+HEIGHT+3) for x,y in tetrominos[t % len(tetrominos)]}
    D |= tet
    direction = {
        '>': (1, 0),
        '<': (-1, 0),
        '^': (0, 1),
        'v': (0, -1)
    }
    rest = False
    while not rest:
        dx, dy = direction[jetpack[pos]]
        D -= tet
        maxx = max(tet)[0]
        minx = min(tet)[0]
        check = 0 <= minx + dx and maxx + dx < LENGTH
        if check:
            for x,y in tet:
                if (x+dx, y+dy) in D:
                    check = False
                    break
        if check:
            tet = {(x+dx, y+dy) for x,y in tet}
        else:
            tet = {(x, y+dy) for x,y in tet}
        for x,y in tet:
            if (x, y-1) in D or y == 0:
                rest = True
                break
        if not rest:
            tet = {(x, y-1) for x,y in tet}
        D |= tet
        pos = (pos + 1) % len(jetpack)
    HEIGHT = max(HEIGHT, max(map(lambda x: x[1]+1, tet)))
    t += 1

h = {}
per = 0
CHECK_ROWS = 15
while not per or t < 2022:
    drop()
    if t == 2022:
        print('Part 1:', HEIGHT)
    top = '\n'.join(''.join(['.#'[int((x, HEIGHT-k-1) in D)] for x in range(0, LENGTH)]) for k in range(CHECK_ROWS))
    if (pos, t % 5, top) in h and not per:
        per = t - h[(pos, t % 5, top)]
    h[(pos, t % 5, top)] = t

# For part 2
pos, t, D, HEIGHT = 0, 0, set(), 0
T = 1000000000000
for _ in range(T % per):
    drop()
h1 = HEIGHT
for _ in range(per):
    drop()
h2 = HEIGHT
# One more time for a good measure
for _ in range(per):
    drop()
h3 = HEIGHT
assert h1 + h3 == 2*h2
per_h = h3 - h2
print('Part 2:', HEIGHT + (T // per - 2) * per_h)