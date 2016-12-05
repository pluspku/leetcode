class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        cnt = 0
        last = None
        for x in nums:
            if x == last:
                cnt += 1
                if cnt <= 2:
                    res.append(x)
            else:
                cnt = 1
                res.append(x)
                last = x
        
        nums[:len(res)] = res
        return len(res)


print Solution().removeDuplicates([1,1,1,2])

