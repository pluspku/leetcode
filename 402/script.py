class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        last = None
        res = []
        k0 = k
        for c in num:
            while res and c < res[-1] and k > 0:
                res.pop()
                k-= 1
            res.append(c)
            last = c
        res = res[:len(num) - k0]
        i = 0
        while i < len(res) and res[i] == '0':
            i += 1
        res = res[i:]

        return ''.join(res) or '0'

fn = Solution().removeKdigits
#print fn("1432219", 3)
#print fn("10200", 1)
#print fn("10", 2)
#print fn("1020300", 2)
#print fn("1234567890", 9)

print fn("9", 1)
