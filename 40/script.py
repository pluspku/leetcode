import json

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        from collections import defaultdict
        X = sorted(candidates)
        fn0 = {(X[0], 1) : [[X[0]]], (0, 0) : [[]]}

        for i, x in enumerate(X[1:]):
            fn1 = {}
            for s, u in fn0:
                if (X[i] != x or u) and s + x <= target:
                    a = []
                    for q in fn0[(s,u)]:
                        v = q[:]
                        v.append(x)
                        a.append(v)
                    fn1.setdefault((s+x, 1), []).extend(a)
                fn1.setdefault((s, 0), []).extend(fn0[(s, u)])
            fn0 = fn1
        return fn0.get((target, 0), []) + fn0.get((target, 1), [])

#C = [10, 1, 2, 7, 6, 1, 5]
#t = 8
C = [4,1,1,4,4,4,4,2,3,5]
t = 10
print Solution().combinationSum2(C, t)

                

        
