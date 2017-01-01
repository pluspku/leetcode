class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N == 0:
            return 1
        for i, x in enumerate(nums):
            if i != x:
                val = nums[0]
                nums[0] = nums[i]
                nums[i] = val

                while nums[0] > 0 and nums[0] < N and nums[0] != nums[nums[0]]:
                    val = nums[nums[0]]
                    nums[nums[0]] = nums[0]
                    nums[0] = val
        last = 0
        for i, x in enumerate(nums):
            if i > 0 and i != x:
                return i
            else:
                last = i
        if nums[0] == N and last == N - 1:
            return N + 1
        else:
            return last + 1

def alter(nums):
    a = sorted(nums)
    last = 0
    for x in a:
        if x > 0:
            if x == last:
                continue
            if x - last == 1:
                last = x
            else:
                return last + 1
    return last + 1


fn = Solution().firstMissingPositive
def test():
    import random
    for t in xrange(1000):
        nums = [random.randint(-100, 100) for i in xrange(20)]
        assert fn(nums[:]) == alter(nums[:]), nums

if __name__ == '__main__':
#    test()
#    nums = [84, 52, 86, 1, -86, -10, 86, 40, -2, -53, -58, 1, -78, 50, -88, 2, 19, -44, -62, 80]
#    print fn(nums[:])
#    print alter(nums[:])
    print fn([1])
