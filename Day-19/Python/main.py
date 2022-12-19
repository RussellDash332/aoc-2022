import sys, re
from collections import deque

bp = {}
for line in sys.stdin:
    idx, o, c, oo, oc, go, gob = map(int, re.findall('Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.', line)[0])
    bp[idx] = (o, c, oo, oc, go, gob)

def solve(idx, time):
    ro, rc, roo, roc, rgo, rgob = bp[idx]
    q = deque([((0, 0, 0, 0, 0, 0, 0, 1), time)])
    states = set()
    ans = 0
    mco = max(rgo, roo, rc, ro)
    while q:
        tup = q[0][0]
        (g, gb, os, osb, c, cb, o, ob), t = q.popleft()

        # t is the time you have left, so simplifying the resources will yield the same outcome
        o = min(o, t*mco)
        c = min(c, t*roc)
        os = min(os, t*rgob)

        # even if we create one new geode robot at a time, it's pointless
        ans = max(g, ans)
        if 2*ans > 2*(g+gb*t) + (t**2-t): continue

        if tup in states: continue
        states.add(tup)
        if t == 1:
            ans = max(g+gb, ans)
            continue

        g2, os2, c2, o2 = g+gb, os+osb, c+cb, o+ob
        # buy geodebot, high priority
        if o >= rgo and os >= rgob:
            q.appendleft(((g2, gb+1, os2-rgob, osb, c2, cb, o2-rgo, ob), t-1))
        # buy obsibot
        if o >= roo and c >= roc:
            q.append(((g2, gb, os2, osb+1, c2-roc, cb, o2-roo, ob), t-1))
        # buy claybot
        if o >= rc:
            q.append(((g2, gb, os2, osb, c2, cb+1, o2-rc, ob), t-1))
        # buy orebot
        if o >= ro:
            q.append(((g2, gb, os2, osb, c2, cb, o2-ro, ob+1), t-1))
        # buy nothing
        q.append(((g2, gb, os2, osb, c2, cb, o2, ob), t-1))
    return ans

print('Part 1:', sum(idx*solve(idx, 24) for idx in bp if idx))
print('Part 2:', solve(1, 32)*solve(2, 32)*solve(3, 32))