
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal > maxChoosableInteger * (maxChoosableInteger+1) / 2:
            return False
        fn = {}
        from math import log
        def sub(stat, h):
            if log(stat) / log(2) >= h:
                print '-1'
                return True
            print stat, h
            for i in xrange(1, maxChoosableInteger + 1):
                if 2**i & stat:
                    s = stat - 2**i
                    r = h - i
                    if (s, r) in fn:
                        flag = fn[(s,r)]
                    else:
                        flag = sub(s, r)
                        fn[(s, r)] = flag
                    if not flag:
                        return True
            return False
        print fn
        return sub(2**(maxChoosableInteger+1)-1, desiredTotal)

print Solution().canIWin(5, 50)
'''
def sub(n, s):
    return Solution().canIWin(n, s)
                        
for n in range(1, 25):
    res = []
    for s in range(1, n * (n + 1) / 2 + 1):
        res.append(sub(n, s))
    print ','.join('%3d' % x for x in res)

'''
