import sys

cont = 0
overlap = 0
for line in sys.stdin:
    a, b = line.split(',')
    (sa, ea), (sb, eb) = map(int, a.split('-')), map(int, b.split('-'))
    cont += (sa <= sb <= eb <= ea) or (sb <= sa <= ea <= eb)
    overlap += (sb <= sa <= eb) or (sa <= sb <= ea)
print('Part 1:', cont)
print('Part 2:', overlap)