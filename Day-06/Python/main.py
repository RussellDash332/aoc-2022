s = input()

def check(l):
    for i in range(len(s)):
        if len(set(s[i:i+l])) == l: return i+l

print('Part 1:', check(4))
print('Part 2:', check(14))