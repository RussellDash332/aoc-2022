import sys

D, T = set(), 0
for e, line in enumerate(sys.stdin):
    for i in range(len(line.strip())):
        if line[i] == '#':
            D.add((e, i))

def check(r, c, f, D, P):
    funcs = [
        lambda x: (r-1, c+1-x) not in D,
        lambda x: (r+1, c+1-x) not in D,
        lambda x: (r+1-x, c-1) not in D,
        lambda x: (r+1-x, c+1) not in D
    ]
    tups = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
    n = 0
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            n += (r+dr, c+dc) in D
    if n == 1: return
    for i in range(f, f+4):
        i %= 4
        if all(map(funcs[i], range(3))):
            P[tups[i]] = P.get(tups[i], []) + [(r, c)]
            return

def tick():
    global T
    P = {}
    for r, c in D:
        check(r, c, T, D, P)
    D2, M = set(), set()
    for r, c in P:
        if len(P[(r, c)]) == 1:
            D2.add((r, c))
            M.add(P[(r, c)][0])
    for r, c in D:
        if (r, c) not in M:
            D2.add((r, c))
    T = (T + 1) % 4
    return D2

R = 10
for _ in range(R):
    D = tick()
minmax = []
for i in range(2):
    minmax.append(min(map(lambda x: x[i], D)))
    minmax.append(max(map(lambda x: x[i], D)))
lr, ur, lc, uc = minmax
print('Part 1:', (ur-lr+1)*(uc-lc+1) - len(D))

R = 10
while True:
    D2 = tick()
    if D == D2: break
    R, D = R+1, D2
print('Part 2:', R+1)