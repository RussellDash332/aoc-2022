import sys

def compare(a1, a2):
    if type(a1) != type(a2):
        if type(a1) != list:
            return compare([a1], a2)
        else:
            return compare(a1, [a2])
    else:
        if type(a1) != list:
            if a1 == a2: return 0
            elif a1 < a2: return 1
            else: return -1
        else:
            for i in range(min(len(a1), len(a2))):
                c = compare(a1[i], a2[i])
                if c != 0: return c
            if len(a1) == len(a2): return 0
            elif len(a1) < len(a2): return 1
            else: return -1

s = ''.join(sys.stdin).strip().split('\n')
rorder = 0
a = []
for i in range(len(s)//3+1):
    a1 = eval(s[3*i])
    a2 = eval(s[3*i+1])
    r = compare(a1, a2)
    if r == 1:
        rorder += i + 1
    a.append(a1)
    a.append(a2)
print('Part 1:', rorder)

a.append([[2]])
a.append([[6]])
# Lazy bubble sort
for i in range(len(a)):
    for j in range(1, len(a)-i):
        if compare(a[j-1], a[j]) == -1:
            a[j-1], a[j] = a[j], a[j-1]
print('Part 2:', (a.index([[2]])+1)*(a.index([[6]])+1))