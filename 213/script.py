class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums) if nums else 0

        f0 = 0
        f1 = 0
        for x in nums[1:]:
            nf0 = max(f1, f0)
            nf1 = f0 + x
            f0 = nf0
            f1 = nf1
        res1 = max(f0, f1)

        f0 = nums[0]
        f1 = nums[0]
        for x in nums[2:-1]:
            nf0 = max(f1, f0)
            nf1 = f0 + x
            f0 = nf0
            f1 = nf1
        res2 = max(f0, f1)
        return max(res1, res2)

import random
nums = [random.randint(0, 10) for x in xrange(10)]
print nums
print Solution().rob(nums)

