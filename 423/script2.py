class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = dict(enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']))
        from collections import Counter
        cnt = Counter(s)
        res = {}
        while chars:
            for i, num in chars.items():
                uniq = set(num) - set().union(*(set(n) for n in chars.values() if n != num))
                if uniq:
                    break

            res[i] = cnt[uniq.pop()]
            for c in num:
                cnt[c] -= res[i]
            del chars[i]
        return ''.join(''.join([str(i)] * res[i]) for i in range(10))



print Solution().originalDigits("owoztneoer")
print Solution().originalDigits("fviefuro")
print Solution().originalDigits("zerozero")
