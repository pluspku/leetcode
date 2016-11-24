class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dat = {}
        for i, c in enumerate(s):
            if c in dat:
                dat[c] = -1
            else:
                dat[c] = i
        vals = [v for v in dat.values() if v >= 0]
        return min(vals) if vals else -1
