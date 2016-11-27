__cache = {}
def cache(fn):
    def wrapper(sets, h):
        k = (tuple(sets), h)
        if k in __cache:
            return __cache[k]
        else:
            res = fn(sets, h)
            __cache[k] = res
            return res
    return wrapper

@cache
def sub(sets, h):
#    print sets, h
    if max(sets) >= h:
        return True
    for i in sets:
        subsets = [x for x in sets if x != i]
        if not sub(subsets, h - i):
            print h, subsets, i
            return True
    return False

'''
for n in range(1, 25):
    res = []
    for s in range(1, n * (n + 1) / 2 + 1):
        res.append(sub(range(1, n+1), s))
    print ','.join('%3d' % x for x in res)
'''         

print sub(range(1, 7), 13)
