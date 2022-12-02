import sys

rps1, rps2 = ['A', 'B', 'C'], ['X', 'Y', 'Z']
ptd = {0: 3, 1: 0, 2: 6}
pts = pts2 = 0
for line in sys.stdin:
    s, e = line.strip().split()
    si, ei = rps1.index(s), rps2.index(e)
    pts += ei + 1 + ptd[(si - ei) % 3]
    out = {0: 1, 1: 0, 2: 2}[ei]
    pts2 += ptd[out] + (si - out) % 3 + 1
print('Part 1:', pts)
print('Part 2:', pts2)