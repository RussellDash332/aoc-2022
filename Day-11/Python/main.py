from collections import deque
import sys, re

s = ''.join(sys.stdin)
its = list(map(lambda x: deque(map(int, x.split(','))), re.findall("Starting items: ([0-9, ]*)", s)))
ops = re.findall("Operation: new = ([^\n]*)", s)
div = list(map(int, re.findall("divisible by (\d+)", s)))
tt = list(map(int, re.findall("true: throw to monkey (\d+)", s)))
ft = list(map(int, re.findall("false: throw to monkey (\d+)", s)))

MOD = 1
for f in div:
    MOD *= f

def simulate(rd, div3):
    items = [i.copy() for i in its]
    ins = [0]*len(items)
    for _ in range(rd):
        for i in range(len(items)):
            for _ in items[i].copy():
                old = items[i].popleft()
                ins[i] += 1
                new = eval(ops[i]) % MOD
                if div3: new //= 3
                items[[ft, tt][int(new % div[i] == 0)][i]].append(new)
    ss = sorted(ins)
    return ss[-1]*ss[-2]

print('Part 1:', simulate(20, True))
print('Part 2:', simulate(10000, False))