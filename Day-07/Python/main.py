import sys

tree = {'/': {}}
path = []
def get_dir(path):
    ptr = tree['/']
    for p in path:
        if p not in ptr:
            ptr[p] = {}
        ptr = ptr[p]
    return ptr

for line in sys.stdin:
    if line.startswith('$'):
        dol, cmd, *args = line.strip().split()
        if cmd == 'cd':
            if args[0] == '..':
                if path: path.pop()
            elif args[0] == '/':
                path.clear()
            else:
                path.append(args[0])
    else:
        t, f = line.strip().split()
        if t == 'dir':
            get_dir(path)[f] = {}
        else:
            get_dir(path)[f] = int(t)

gsz = 0
dsz = []
def get_size(lb, tree):
    global gsz
    sz = 0
    for k, v in tree.items():
        if type(v) == dict:
            isz = get_size(lb, v)
            dsz.append([k, isz])
            sz += isz
        else:
            sz += v
    if sz <= lb:
        gsz += sz
    return sz

asz = get_size(100000, tree)
print('Part 1:', gsz)
dsz = list(filter(lambda x: x[1] >= asz - 4e7, dsz))
print('Part 2:', min(dsz, key=lambda x: x[1])[1])