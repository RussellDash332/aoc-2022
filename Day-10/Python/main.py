import sys

xl, x, cyc = [], 1, 0
m = [['.' for _ in range(40)] for _ in range(6)]
def write():
    m[cyc//40][cyc%40] = '.#'[int(cyc%40 in [x-1,x,x+1])]

for line in sys.stdin:
    cmd = line.strip().split()
    if cmd[0] == 'noop':
        xl.append(x)
        write()
        cyc += 1
    else:
        xl.append(x)
        write()
        cyc += 1
        write()
        x += int(cmd[1])
        xl.append(x)
        cyc += 1

def ss(c):
    return c*xl[c-2]

print('Part 1:', sum(map(ss, [40*i+20 for i in range(6)])))
print('Part 2:')
for r in m:
    print(''.join(r))