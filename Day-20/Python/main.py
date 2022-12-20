import sys

arr = []
for line in sys.stdin:
    arr.append((int(line), len(arr)))
    if arr[-1][0] == 0: ii = arr[-1][1]
arr2 = list(map(lambda x: (811589153*x[0], x[1]), arr))
order = arr.copy()
order2 = arr2.copy()

def mix(arr, order):
    n = len(arr) - 1
    for i in order:
        if i[0] == 0: continue
        t = arr.index(i)
        arr.pop(t)
        arr.insert((t + i[0]) % n, i)

def solve(arr, order, it):
    for _ in range(it): mix(arr, order)
    z = arr.index((0, ii))
    return sum(arr[(z + 1000*(i+1)) % len(arr)][0] for i in range(3))

print('Part 1:', solve(arr, order, 1))
print('Part 2:', solve(arr2, order2, 10))
