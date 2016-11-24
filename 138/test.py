from script import Solution, RandomListNode
import random

def plist(root):
    print "%s(%s) ->" % (root.label, root.random.label if root.random else None)
    if root.next:
        plist(root.next)

N = 10
tbl = {}
for i in xrange(N):
    tbl[i] = RandomListNode(i)
    if i > 0:
        tbl[i-1].next = tbl[i]

for i in xrange(N):
    r = random.randint(0, N)
    if r != N:
        tbl[i].random = tbl[r]

plist(tbl[0])
p = Solution().copyRandomList(tbl[0])
print '=============='
plist(p)
