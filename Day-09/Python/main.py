import sys

moves = []
d = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
for line in sys.stdin:
    a, b = line.split()
    moves.append((d[a], int(b)))
hr, hc, tr, tc = 0, 0, 0, 0
diff = {-2: -1, 2: 1}
def simulate(hr, hc, knots):
    vis = set()
    pos = [[hr, hc] for _ in range(knots)]
    for move in moves:
        (dr, dc), f = move
        for _ in range(f):
            pos[0][0] += dr
            pos[0][1] += dc
            for i in range(1, knots):
                diffr = pos[i-1][0]-pos[i][0]
                diffc = pos[i-1][1]-pos[i][1]
                if abs(diffr) > 1 or abs(diffc) > 1:
                    pos[i][0] += diff.get(diffr, diffr)
                    pos[i][1] += diff.get(diffc, diffc)
            vis.add(tuple(pos[-1]))
    return len(vis)
print('Part 1:', simulate(0, 0, 2))
print('Part 2:', simulate(0, 0, 10))