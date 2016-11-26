class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def sub(prefix, d, v):
            if d + v == 0:
                res.append(prefix)
            else:
                if d:
                    sub(prefix + '(', d - 1, v + 1)
                if v:
                    sub(prefix + ')', d , v - 1)
        sub('', n, 0)
        return res


print Solution().generateParenthesis(3)

