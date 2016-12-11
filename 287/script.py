class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = nums[0]
        f = nums[nums[0]]
        while f!=s:
            f = nums[nums[f]]
            s = nums[s]

        f = 0
        while f != s:
            f = nums[f]
            s = nums[s]
        return f



print Solution().findDuplicate([1,3,4,2,2])
