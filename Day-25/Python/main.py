import sys

D = {'0': 0, '1': 1, '2': 2, '-': -1, '=': -2}
E = dict(map(reversed, D.items()))

def desnafu(s):
    r = 0
    for i in s.strip(): r = 5*r + D[i]
    return r

def snafu(n):
    s = []
    while n:
        s.append(E[n%5 - 5*(n%5>2)])
        n = n//5 + (n%5>2)
    return ''.join(s[::-1])

print('Part 1:', snafu(sum(map(desnafu, sys.stdin))))
print('Part 2: THE END!')