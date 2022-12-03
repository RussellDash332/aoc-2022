import sys, string

ps = g = 0
letters = string.ascii_lowercase + string.ascii_uppercase
groups = []
for line in sys.stdin:
    if g == 0:
        groups.append(set(letters))
    line = line.strip()
    common = list(set(line[:len(line)//2]) & set(line[len(line)//2:]))[0]
    ps += (ord(common) - 38) if ord(common) < 98 else (ord(common) - 96)
    groups[-1] &= set(line)
    g = (g + 1) % 3
print('Part 1:', ps)
print('Part 2:', sum((ord(common) - 38) if ord(common) < 98 else (ord(common) - 96) for common in map(lambda x: list(x)[0], groups)))