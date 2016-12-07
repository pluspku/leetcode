class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        m = float('inf')
        for i, x in enumerate(nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(m - target):
                    m = s
                if s == target:
                    return target
                elif s < target:
                    j += 1
                else:
                    k -= 1
        return m


print Solution().threeSumClosest([-1, 2, 1, -4], 2)
#print Solution().threeSumClosest([0,0,0], 1)

