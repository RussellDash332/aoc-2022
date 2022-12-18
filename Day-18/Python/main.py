import sys
from collections import defaultdict

C = defaultdict(lambda: 0)
for line in sys.stdin:
    x, y, z = map(lambda p: 2*int(p), line.split(','))
    for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
        C[(x+dx, y+dy, z+dz)] += 1
print('Part 1:', sum([v == 1 for k, v in C.items()]))

minmax = []
for i in range(3):
    minmax.append(min(map(lambda x: x[i]//2*2-2, C)))
    minmax.append(max(map(lambda x: x[i]//2*2+2, C)))
minx, maxx, miny, maxy, minz, maxz = minmax
Q = [(minx, miny, minz)]
L, V = set(), set()
while Q:
    x, y, z = Q.pop()
    if (x, y, z) in V: continue
    V.add((x, y, z))
    if not (minx-2 <= x <= maxx+2 and miny-2 <= y <= maxy+2 and minz-2 <= z <= maxz+2): continue
    for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
        if (x+dx, y+dy, z+dz) not in C:
            Q.append((x+2*dx, y+2*dy, z+2*dz))
        else:
            L.add((x+dx, y+dy, z+dz))
print('Part 2:', len(L))