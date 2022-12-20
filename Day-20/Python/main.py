import sys

arr = []
for line in sys.stdin:
    arr.append((int(line), len(arr)))
    if arr[-1][0] == 0: ii = arr[-1][1]

def mix(arr, order):
    n = len(arr) - 1
    for i in order:
        if i[0] == 0: continue
        t = arr.index(i)
        arr.pop(t)
        arr.insert((t + i[0]) % n, i)

def solve(arr, mult, it):
    arr = [(a*mult, b) for a,b in arr]
    order = arr.copy()
    for _ in range(it): mix(arr, order)
    z = arr.index((0, ii))
    return sum(arr[(z + 1000*(i+1)) % len(arr)][0] for i in range(3))

print('Part 1:', solve(arr, 1, 1))
print('Part 2:', solve(arr, 811589153, 10))