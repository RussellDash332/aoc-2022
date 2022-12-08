import sys

m = []
for line in sys.stdin:
    m.append(list(map(int, line.strip())))

visible = set()
ri, rj = [range(len(m)), range(len(m)-1,-1,-1)], [range(len(m[0])), range(len(m[0])-1,-1,-1)]
for r in ri:
    for i in r:
        for s in rj:
            c = -1
            for j in s:
                if m[i][j] >= c:
                    if m[i][j] > c:
                        visible.add((i, j))
                    c = m[i][j]
for r in rj:
    for j in r:
        for s in ri:
            c = -1
            for i in s:
                if m[i][j] >= c:
                    if m[i][j] > c:
                        visible.add((i, j))
                    c = m[i][j]
print('Part 1:', len(visible))

def ss(i, j):
    s = 1
    for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        ci, cj, d = i, j, 0
        while 0 <= ci  + dr < len(m) and 0 <= cj + dc < len(m[0]):
            if m[i][j] > m[ci + dr][cj + dc]:
                d += 1
                ci += dr
                cj += dc
            else:
                d += 1
                break
        s *= d
    return s
print('Part 2:', max(ss(i, j) for i in range(len(m)) for j in range(len(m[0]))))