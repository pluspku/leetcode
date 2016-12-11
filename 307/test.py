from script import NumArray as T
from trivial import NumArray as B

import random
N = 1000
nums = range(N)

t = T(nums)
b = B(nums)
for z in xrange(1000):
    i = random.randint(0, N-1)
    val = random.randint(0, 101)
    b.update(i, val)
    t.update(i, val)

    i = random.randint(0, N-1)
    j = random.randint(i, N-1)
    assert b.sumRange(i, j) == t.sumRange(i, j)



print 'test passed'
