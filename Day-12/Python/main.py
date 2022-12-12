from collections import deque
import sys

s = []
for line in sys.stdin:
    s.append(list(line.strip()))
srcs = []

for i in range(len(s)):
    s[i] = list(s[i])
    for j in range(len(s[0])):
        if s[i][j] == 'S':
            s[i][j] = chr(96)
            src = (i, j)
        elif s[i][j] == 'E':
            s[i][j] = chr(123)
            dst = (i, j)
        elif s[i][j] == 'a':
            srcs.append((i, j))

def bfs(q, part):
    vis = set()
    while q:
        (r, c), d = q.popleft()
        if (r, c) == dst:
            print(f'Part {part}:', d)
            break
        if (r, c) in vis:
            continue
        vis.add((r, c))
        for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
            if 0 <= r+dr < len(s) and 0 <= c+dc < len(s[0]):
                if ord(s[r+dr][c+dc]) - ord(s[r][c]) <= 1:
                    q.append(((r+dr, c+dc), d+1))
                    
bfs(deque([(src, 0)]), 1)
bfs(deque([(src, 0) for src in srcs]), 2)