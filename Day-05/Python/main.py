import sys
from copy import deepcopy

lines = []

for line in sys.stdin:
    lines.append([line[4*i:4*i+3] for i in range(len(line))])
    if not line.strip(): break
nstacks = lines[-2].index('\n')
stacks = [[] for _ in range(nstacks)]
for line in lines[-3::-1]:
    for i in range(nstacks):
        if line[i].strip():
            stacks[i].append(line[i][1])

stacks2 = deepcopy(stacks)
for line in sys.stdin:
    d, a, f, b, t, c = line.split()
    a, b, c = map(int, [a, b, c])
    for _ in range(a):
        stacks[c-1].append(stacks[b-1].pop())
    stacks2[c-1].extend(stacks2[b-1][-a:])
    stacks2[b-1] = stacks2[b-1][:-a]
print('Part 1:', ''.join([s[-1] for s in stacks]))
print('Part 2:', ''.join([s[-1] for s in stacks2]))