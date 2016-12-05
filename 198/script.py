class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r0 = 0
        r1 = 0
        for x in nums:
            nr1 = r0 + x
            nr0 = max(r0, r1)
            r0 = nr0
            r1 = nr1
        return max(r0, r1)

print Solution().rob([1,2,3,4,5,6,7])
