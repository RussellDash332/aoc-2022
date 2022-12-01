import sys

cals = [0]
for line in sys.stdin:
    try:    cals[-1] += int(line)
    except: cals.append(0)
print('Part 1:', max(cals))
print('Part 2:', sum(sorted(cals)[-3:]))