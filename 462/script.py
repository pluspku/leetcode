class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        X = sorted(nums)
        i = len(nums) / 2
        v = X[i]
        return sum(abs(x - v) for x in nums)


print Solution().minMoves2([1,2,4,6])
