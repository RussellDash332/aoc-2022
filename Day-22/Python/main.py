import sys, os, shutil
from copy import deepcopy

# For visualization
try: shutil.rmtree('frames')
except: pass
os.makedirs('frames', exist_ok=True)
from PIL import Image
from PIL import ImageDraw
import imageio

SIZE = 50

D, U, U2, L, L2 = {}, {}, {}, {}, {}
F = {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}
A = {(0, 1): '>', (1, 0): 'v', (0, -1): '<', (-1, 0): '^'}

m = []
for e, line in enumerate(sys.stdin):
    line = ' '*SIZE + line.strip('\r\n') + ' '*SIZE
    if not line.strip(): break
    m.append(list(line))
    l = 0
    for i in range(len(line)):
        if l == 0 and line[i] != ' ':   L[e], l = i, 1
        if line[i] != ' ':              U[e] = i
        if line[i] == '.':              D[(e, i)] = 1
        elif line[i] == '#':            D[(e, i)] = 0
m2 = deepcopy(m)

def draw(p=None):
    res = '\n'.join(map(lambda r: ''.join(r[SIZE:-SIZE]), m))
    if p == None: print(res)
    else:
        if p.endswith('.txt'):
            open(p, 'w+').write(res)
        elif p.endswith('.png'):
            img = Image.new('RGB', (6*(max(map(len, m))-2*SIZE), 15*len(m)))
            d = ImageDraw.Draw(img)
            d.text((0, 0), res, fill=(255, 255, 255))
            img.save(open(p, 'wb+'), 'png')
    return res

def make_gif(p):
    with imageio.get_writer(p, mode='I') as writer:
        for filename in os.listdir('frames'):
            print(filename)
            image = imageio.imread(os.path.join('frames', filename))
            writer.append_data(image)
    for filename in os.listdir('frames'):
        os.remove(os.path.join('frames', filename))

for i in range(max(U.values()) + 1):
    l = 0
    for j in range(len(U)):
        if l == 0 and (j, i) in D:  L2[i], l = j, 1
        if (j, i) in D:             U2[i] = j

cmds = []
tmp = [s.split('L') for s in input().split('R')]
for cmd in tmp:
    for mag in cmd:
        cmds.append(int(mag))
        cmds.append('L')
    cmds[-1] = 'R'
cmds.pop()

# No I did not list all the cases, try this at your own risk.
def simulate(faces=[], draw_fp=None):
    # (0, L[0]) is guaranteed to be '.'?
    r, c, dr, dc = 0, L[0], 0, 1
    frame = 0
    for cmd in cmds:
        if cmd == 'L':      dr, dc = -dc, dr
        elif cmd == 'R':    dr, dc = dc, -dr
        else:
            for _ in range(cmd):
                m[r][c] = A[(dr, dc)]
                odr, odc = dr, dc
                nr, nc = r+dr, c+dc
                if not faces:
                    if dr == 0:
                        if nc < L[r]:       nc = U[r]
                        elif nc > U[r]:     nc = L[r]
                    else: # dc == 0:
                        if nr < L2[c]:      nr = U2[c]
                        elif nr > U2[c]:    nr = L2[c]
                else:
                    face = C * (nr // SIZE) + nc // SIZE
                    if face not in faces:
                        if F[(dr, dc)] == 0: # facing right
                            if face + C in faces: # down
                                f = face + C
                                dr, dc = dc, -dr
                                nr, nc = f//C*SIZE + nc%SIZE, f%C*SIZE + (SIZE-1-nr%SIZE)
                            elif face - C in faces: # up
                                f = face - C
                                dr, dc = -dc, dr
                                nr, nc = f//C*SIZE + (SIZE-1-nc%SIZE), f%C*SIZE + nr%SIZE
                            elif face - 2*C in faces: # 2*up
                                f = face - 2*C
                                dr, dc = dr, -dc
                                nr, nc = f//C*SIZE + (SIZE-1-nr%SIZE), f%C*SIZE + (SIZE-1-nc%SIZE)
                            elif face + 2*C - 2 in faces: # 2*down - 2
                                f = face + 2*C - 2
                                dr, dc = dr, -dc
                                nr, nc = f//C*SIZE + (SIZE-1-nr%SIZE), f%C*SIZE + (SIZE-1-nc%SIZE)
                        elif F[(dr, dc)] == 1: # facing down
                            if face - 1 in faces: # -1
                                f = face - 1
                                dr, dc = dc, -dr
                                nr, nc = f//C*SIZE + nc%SIZE, f%C*SIZE + (SIZE-1-nr%SIZE)
                            elif face - 2*C - 2 in faces: # 2*up-2
                                f = face - 2*C - 2
                                dr, dc = -dr, dc
                                nr, nc = f//C*SIZE + (SIZE-1-nr%SIZE), f%C*SIZE + (SIZE-1-nc%SIZE)
                            elif face - R*C + 2 in faces:
                                f = face - R*C + 2
                                nr, nc = f//C*SIZE + nr%SIZE, f%C*SIZE + nc%SIZE
                        elif F[(dr, dc)] == 2: # facing left
                            if face - (R-1)*C + 2 in faces:
                                f = face - (R-1)*C + 2
                                dr, dc = -dc, dr
                                nr, nc = f//C*SIZE + (SIZE-1-nc%SIZE), f%C*SIZE + nr%SIZE
                            elif face + C in faces: # down
                                f = face + C
                                dr, dc = -dc, dr
                                nr, nc = f//C*SIZE + (SIZE-1-nc%SIZE), f%C*SIZE + nr%SIZE
                            elif face + 2*C in faces: # 2*down
                                f = face + 2*C
                                dr, dc = dr, -dc
                                nr, nc = f//C*SIZE + (SIZE-1-nr%SIZE), f%C*SIZE + (SIZE-1-nc%SIZE)
                            elif face - 2*C + 2 in faces: # 2*up+2
                                f = face - 2*C + 2
                                dr, dc = dr, -dc
                                nr, nc = f//C*SIZE + (SIZE-1-nr%SIZE), f%C*SIZE + (SIZE-1-nc%SIZE)
                        elif F[(dr, dc)] == 3: # facing up
                            if face + 1 in faces: # +1
                                f = face + 1
                                dr, dc = dc, -dr
                                nr, nc = f//C*SIZE + nc%SIZE, f%C*SIZE + (SIZE-1-nr%SIZE)
                            elif face + R*C - 1 in faces: # +R*C-1
                                f = face + R*C - 1
                                dr, dc = dc, -dr
                                nr, nc = f//C*SIZE + nc%SIZE, f%C*SIZE + (SIZE-1-nr%SIZE)
                            elif face + R*C - 2 in faces: # +R*C-2
                                f = face + R*C - 2
                                nr, nc = f//C*SIZE + nr%SIZE, f%C*SIZE + nc%SIZE
                if D[(nr, nc)]:
                    r, c = nr, nc
                else:
                    dr, dc = odr, odc
            if draw_fp != None: draw(f'frames/frame_{str(frame).zfill(7)}.png')
            frame += 1
    if draw_fp != None: make_gif(draw_fp)
    return 1000*(r+1) + 4*(c+1-SIZE) + F[(dr, dc)]

faces = []
R = (max(U2.values()) + 1) // SIZE
C = (max(U.values()) + 1) // SIZE + 1
for r in range(R):
    for c in range(C):
        if (SIZE*r, SIZE*c) in D:
            faces.append(C*r + c)

print('Part 1:', simulate())
#print('Part 1:', simulate(draw_fp='d22p1.gif'))
draw('part1.txt')

m = m2
print('Part 2:', simulate(faces))
#print('Part 2:', simulate(faces, draw_fp='d22p2.gif'))
draw('part2.txt')

shutil.rmtree('frames')