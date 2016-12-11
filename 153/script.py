class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        l = 0
        r = len(nums)
        while r - l > 1:
            m = (l + r) / 2
            if nums[m] < nums[l]:
                r = m
            else:
                l = m
        m = ((l + r) / 2 + 1) % len(nums)
        return nums[m]

N = 20
for i in xrange(N):
    a = range(N)
    a = a[i:N] + a[:i]
    print Solution().findMin(a)


print Solution().findMin([1])
