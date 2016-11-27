class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        intvs = []
        m1 = None
        m2 = None
        
        for x in nums:
            if m2 is None:
                m1 = x
                m2 = x
            elif x > m2:
                m2 = x
                intvs = [[m1, m2]]
            elif x < m1:
                m1 = x
            else:
                updated = False
                for intv in intvs:
                    if x >= intv[1]:
                        updated = True
                        intv[1] = x
                        break
                    elif x > intv[0]:
                        return True
                if not updated:
                    intvs.append([m1, x])
        return False

print Solution().find132pattern([1,0,1,-4,-3])
print Solution().find132pattern([3,5,0,3,4])
print Solution().find132pattern([-2, 0, -2])

