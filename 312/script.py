class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        fn = {}
        nums = [1] + nums + [1]
        N = len(nums)
        for d in xrange(2, N):
            for i in xrange(N - d):
                j = i + d
                m = 0
                for k in xrange(i+1, j):
                    m = max(m, fn.get((i,k), 0) + fn.get((k, j), 0) + nums[i] * nums[k] * nums[j])
                fn[(i,j)] = m
        return fn[(0, N-1)]
        

print Solution().maxCoins([7,9,8,0,7,1,3,5])



            

 
