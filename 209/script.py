class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        x = 0
        m = len(nums) + 1
        for j in xrange(len(nums)):
            x += nums[j]
            while x - nums[i] >= s:
                x -= nums[i]
                i += 1
            if j - i + 1 < m and x >= s:
                m = j - i + 1
        return m if m <= len(nums) else 0


print Solution().minSubArrayLen(7, [2,3,1,2,4,3])
