import sys, re
from collections import deque

g, ff = {}, {}

for line in sys.stdin:
    res = re.findall('Valve (\w+) has flow rate=(\d+); tunnel[s]* lead[s]* to valve[s]* ([\w\s,]*)', line.strip())[0]
    u, f, vv = res
    f = int(f)
    vv = vv.split(', ')
    ff[u] = f
    g[u] = vv

q = deque([(0, 'AA', [], 0)])
TIME = 30
states = set()
ps = {i: {} for i in range(TIME+1)}
while q:
    t, s, p, pp = q.popleft()
    tup = (t, s, pp, len(p)) # accurate: tuple(sorted(p))
    if tup in states: continue
    states.add(tup)
    if t == TIME + 1: break
    ip = sum(map(ff.get, p))
    tt = tuple(sorted(p))
    if t <= TIME: ps[t][tt] = max(ps[t].get(tt, 0), pp)
    if s not in p and ff[s] != 0:
        q.append((t+1, s, p+[s], pp+ip))
    for d in g[s]: q.append((t+1, d, p, pp+ip))
ans = max(ps[30].values())
print('Part 1:', ans)

ans = max(ans, max(ps[26][i] + ps[26][j] for i in ps[26] for j in ps[26] if not set(i) & set(j)))
print('Part 2:', ans)