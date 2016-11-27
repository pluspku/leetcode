class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import Counter
        c1 = Counter([x + y for x in A for y in B])
        c2 = Counter([-x - y for x in C for y in D])
        cnt = sum(c1[s] * c2[s] for s in c1)
        return cnt

#print Solution().fourSumCount([ 1, 2], [-2,-1], [-1,2], [0,2])
print Solution().fourSumCount([-1,-1], [-1, 1], [-1,1], [1,-1])

