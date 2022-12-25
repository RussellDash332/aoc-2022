import sys, os, shutil
from collections import deque
from copy import deepcopy

# For visualization
try: shutil.rmtree('frames')
except: pass
os.makedirs('frames', exist_ok=True)
from PIL import Image
from PIL import ImageDraw
import imageio

m = []
for line in sys.stdin:
    m.append(list(line.strip()))

R, C = len(m), len(m[0])
sr, sc = 0, 1
gr, gc = R-1, C-2

A = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}
A2 = {(0, 1): '>', (1, 0): 'v', (0, -1): '<', (-1, 0): '^'}
B = {}
b = 0
for i in range(R):
    for j in range(C):
        if m[i][j] in '<v^>':
            B[(i, j)] = B.get((i, j), []) + [(b, *A[m[i][j]])]
            b += 1

def draw(p=None):
    m2 = deepcopy(m)
    m2[0][1] = '.'
    for i in range(1, R-1):
        for j in range(1, C-1):
            if (i, j) not in B:
                m2[i][j] = '.'
            elif len(B[(i, j)]) == 1:
                m2[i][j] = A2[B[(i, j)][0][1:]]
            else:
                m2[i][j] = str(len(B[(i, j)]))
    res = '\n'.join(map(''.join, m2))
    if p == None: print(res)
    else:
        if p.endswith('.txt'):
            open(p, 'w+').write(res)
        elif p.endswith('.png'):
            img = Image.new('RGB', (6*C, 15*R))
            d = ImageDraw.Draw(img)
            d.text((0, 0), res, fill=(255, 255, 255))
            img.save(open(p, 'wb+'), 'png')
    return res

def make_gif(p):
    with imageio.get_writer(p, mode='I') as writer:
        for filename in os.listdir('frames'):
            image = imageio.imread(os.path.join('frames', filename))
            writer.append_data(image)
    for filename in os.listdir('frames'):
        os.remove(os.path.join('frames', filename))

N = ((-1, 0), (0, -1), (1, 0), (0, 1), (0, 0))
Q = deque([(sr, sc, 0)])
p, states = None, set()

def tick():
    global B, Q, p, states
    B2, Q2 = {}, deque()
    for (rr, cc), pts in B.items():
        for idx, dr, dc in pts:
            nr, nc = rr+dr, cc+dc
            if nc == len(m[0])-1: nc = 1
            elif nc == 0: nc = len(m[0])-2
            if nr == len(m)-1: nr = 1
            elif nr == 0: nr = len(m)-2
            B2[(nr, nc)] = B2.get((nr, nc), []) + [(idx, dr, dc)]
    B, B2 = B2, B
    while Q:
        r, c, t = Q.popleft()
        if (r, c, t) in states: continue
        states.add((r, c, t))
        if not p and (r, c) == (gr, gc):
            p = t
            B = B2
            return
        for dr, dc in N:
            if 0 <= r+dr < R and 0 <= c+dc < C:
                if m[r+dr][c+dc] != '#' and (r+dr, c+dc) not in B:
                    Q2.append((r+dr, c+dc, t+1))
    Q = Q2
    #draw(f'frames/frame_{str(t).zfill(5)}.png')

while not p:
    tick()
print('Part 1:', p)

for _ in range(2):
    Q, p, states = deque([(gr, gc, p)]), None, set()
    sr, sc, gr, gc = gr, gc, sr, sc
    while not p:
        tick()
print('Part 2:', p)
#make_gif('d24.gif')