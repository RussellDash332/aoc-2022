import sys
from z3 import *

cmds, vv = [], []
for line in sys.stdin:
    n, op = line.strip().split(': ')
    if n == 'humn':     ii = len(cmds)
    elif n == 'root':   jj = len(cmds)
    cmds.append(f'{n} = {op}')
    vv.append(n)
while True:
    for cmd in cmds:
        try: exec(cmd)
        except: pass
    try:
        print('Part 1:', int(root))
        break
    except: pass

for v in vv: del globals()[v]
cmds.pop(ii)
vv.pop(ii)
humn = Int('x')
while True:
    for cmd in cmds:
        try: exec(cmd)
        except: pass
    try:
        op = cmds[jj].split('= ')[1].split(' + ')
        v1, v2 = [eval(i) for i in op]
        s = Solver()
        s.add(v1 == v2)
        assert s.check() == sat
        print('Part 2:', s.model()[humn])
        break
    except: pass